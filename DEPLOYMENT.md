# Deployment Guide

This guide covers multiple deployment options for the SkillPath application.

## Local Development

### Quick Start

1. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Start the Flask server:
```bash
python app.py
```

3. Open `frontend/index.html` in your browser or serve it:
```bash
cd frontend
python -m http.server 8000
```

Visit `http://localhost:8000`

### Using the Startup Script

Make the script executable and run:
```bash
chmod +x start.sh
./start.sh
```

## Production Deployment

### Option 1: Heroku

#### Backend Deployment

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create skillpath-backend
```

3. Set environment variables:
```bash
heroku config:set OPENROUTER_API_KEY=your_api_key_here
```

4. Deploy:
```bash
git push heroku main
```

5. Note your backend URL (e.g., `https://skillpath-backend.herokuapp.com`)

#### Frontend Deployment

Update `API_BASE` in `frontend/app.js`:
```javascript
const API_BASE = 'https://skillpath-backend.herokuapp.com';
```

Then deploy to Netlify, Vercel, or GitHub Pages.

### Option 2: Railway

1. Install Railway CLI:
```bash
npm i -g @railway/cli
```

2. Login and initialize:
```bash
railway login
railway init
```

3. Set environment variables:
```bash
railway variables set OPENROUTER_API_KEY=your_api_key_here
```

4. Deploy:
```bash
railway up
```

### Option 3: DigitalOcean App Platform

1. Create a new app from your Git repository
2. Configure build settings:
   - Build Command: `pip install -r backend/requirements.txt`
   - Run Command: `cd backend && python app.py`
3. Add environment variable `OPENROUTER_API_KEY`
4. Deploy

### Option 4: AWS EC2

1. Launch an EC2 instance (Ubuntu 22.04)

2. SSH into your instance and install dependencies:
```bash
sudo apt update
sudo apt install python3-pip nginx
```

3. Clone your repository:
```bash
git clone your-repo-url
cd your-repo
```

4. Install Python dependencies:
```bash
cd backend
pip3 install -r requirements.txt
pip3 install gunicorn
```

5. Create a systemd service file `/etc/systemd/system/skillpath.service`:
```ini
[Unit]
Description=SkillPath Flask App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/your-repo/backend
Environment="OPENROUTER_API_KEY=your_key_here"
ExecStart=/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

6. Start the service:
```bash
sudo systemctl start skillpath
sudo systemctl enable skillpath
```

7. Configure Nginx as reverse proxy:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /home/ubuntu/your-repo/frontend;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
}
```

### Option 5: Docker Deployment

Create `Dockerfile` in the backend directory:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t skillpath-backend ./backend
docker run -p 5000:5000 -e OPENROUTER_API_KEY=your_key skillpath-backend
```

## Frontend Deployment Options

### Netlify

1. Install Netlify CLI:
```bash
npm install -g netlify-cli
```

2. Update `API_BASE` in `frontend/app.js` to your backend URL

3. Deploy:
```bash
cd frontend
netlify deploy --prod
```

### Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Update `API_BASE` in `frontend/app.js`

3. Deploy:
```bash
cd frontend
vercel --prod
```

### GitHub Pages

1. Update `API_BASE` in `frontend/app.js`

2. Push to GitHub

3. Go to Settings > Pages

4. Select branch and `/frontend` folder

5. Save and wait for deployment

### Cloudflare Pages

1. Connect your Git repository

2. Build settings:
   - Build command: (leave empty)
   - Build output directory: `/frontend`

3. Deploy

## Environment Variables

For production, always use environment variables for sensitive data:

```python
import os

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
```

## CORS Configuration

If you deploy frontend and backend on different domains, update CORS settings in `backend/app.py`:

```python
CORS(app, origins=[
    "https://your-frontend-domain.com",
    "http://localhost:8000"  # for local development
])
```

## Monitoring & Logging

For production deployments, consider:

1. Application monitoring (New Relic, DataDog)
2. Error tracking (Sentry)
3. Logging (CloudWatch, Papertrail)
4. Uptime monitoring (UptimeRobot)

## Security Checklist

- [ ] Use environment variables for API keys
- [ ] Enable HTTPS
- [ ] Configure proper CORS settings
- [ ] Add rate limiting
- [ ] Implement API authentication if needed
- [ ] Regular security updates
- [ ] Input validation and sanitization

## Performance Optimization

1. Enable gzip compression
2. Use CDN for static assets
3. Implement caching strategies
4. Optimize images
5. Minify CSS and JavaScript
6. Use connection pooling for database

## Troubleshooting

### Backend not starting
- Check Python version (3.8+)
- Verify all dependencies installed
- Check firewall settings
- Review error logs

### Frontend can't connect to backend
- Verify API_BASE URL is correct
- Check CORS configuration
- Ensure backend is running
- Check network/firewall rules

### AI features not working
- Verify OPENROUTER_API_KEY is set
- Check API key is valid
- Review API rate limits
- Check error logs

## Support

For deployment issues, check the logs and refer to the platform-specific documentation.
