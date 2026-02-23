# Quick Start Guide

Get SkillPath running in under 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser

## Installation Steps

### Step 1: Install Backend Dependencies

Open a terminal and navigate to the backend directory:

```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start the Backend Server

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

Keep this terminal window open.

### Step 3: Open the Frontend

Open a new terminal window and navigate to the frontend directory:

```bash
cd frontend
```

Then start a simple HTTP server:

**Using Python:**
```bash
python -m http.server 8000
```

**Using Python 3 explicitly:**
```bash
python3 -m http.server 8000
```

**Using Node.js (if installed):**
```bash
npx http-server -p 8000
```

### Step 4: Access the Application

Open your web browser and go to:
```
http://localhost:8000
```

## Quick Test

1. Type "Python" in the skill input field
2. Click "Generate" button
3. You should see a learning roadmap appear
4. Click on any node to see details and resources

## Alternative: One-Line Startup

If you're on Linux or macOS, you can use the startup script:

```bash
chmod +x start.sh
./start.sh
```

## Alternative: Docker

If you have Docker installed:

```bash
docker-compose up
```

Access the app at `http://localhost:8080`

## Troubleshooting

### Backend won't start

**Error: Module not found**
```bash
pip install -r backend/requirements.txt
```

**Error: Port 5000 already in use**
- Stop any other application using port 5000
- Or change the port in `backend/app.py`: `app.run(debug=True, port=5001)`

### Frontend issues

**Cannot access localhost:8000**
- Make sure you started the HTTP server
- Try a different port: `python -m http.server 8080`
- Or simply open `frontend/index.html` directly in your browser

**Roadmap generation fails**
- Check that the backend is running on port 5000
- Open browser console (F12) to see error messages
- Verify `backend/roadmaps_master.json` exists

### AI features not working

The AI explanation and chat features require an OpenRouter API key. The app will still work for roadmap generation and certifications without it.

To enable AI features:
1. Get an API key from [OpenRouter](https://openrouter.ai/)
2. Update `OPENROUTER_API_KEY` in `backend/app.py` or set as environment variable

## What's Next?

Check out:
- `README.md` for full documentation
- `DEPLOYMENT.md` for production deployment options
- Customize roadmaps in `backend/roadmaps_master.json`

## Testing the Backend

Run the test suite:
```bash
python test_backend.py
```

Make sure the backend is running before executing tests.

## Default Roadmaps Available

- Python
- JavaScript
- Web Development
- Data Science

Add more in `backend/roadmaps_master.json`!

## Need Help?

1. Check error messages in the terminal
2. Open browser console (F12) for frontend errors
3. Review the README.md for detailed documentation
4. Check the issues in the project repository

Happy Learning!
