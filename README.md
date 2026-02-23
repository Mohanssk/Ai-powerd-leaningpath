# SkillPath - AI-Powered Learning Roadmaps

A full-stack application that generates personalized learning roadmaps with AI-powered explanations and free certification recommendations.

## Features

- Generate learning roadmaps for various skills
- AI-powered explanations for each learning node
- Free certification and course recommendations
- Interactive AI mentor chatbot
- Clean and modern UI with Tailwind CSS

## Tech Stack

### Frontend
- HTML5
- Tailwind CSS
- Vanilla JavaScript

### Backend
- Python 3.8+
- Flask
- Flask-CORS
- OpenRouter API for AI features

## Project Structure

```
project/
├── frontend/
│   ├── index.html      # Main HTML file
│   └── app.js          # Frontend JavaScript logic
├── backend/
│   ├── app.py          # Flask backend server
│   ├── sanitize.py     # Data sanitization utility
│   ├── requirements.txt # Python dependencies
│   └── roadmaps_master.json # Roadmap data
└── README.md           # This file
```

## Installation & Setup

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python app.py
```

The backend will start on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Open `index.html` in your browser, or serve it using a simple HTTP server:

Using Python:
```bash
python -m http.server 8000
```

Using Node.js (if you have `http-server` installed):
```bash
npx http-server -p 8000
```

3. Open `http://localhost:8000` in your browser

## Usage

### Generate a Roadmap

1. Enter a skill in the input field (e.g., "Python", "JavaScript", "Web Development", "Data Science")
2. Click "Generate" or press Enter
3. View the learning path with numbered nodes
4. Click on any node to see:
   - AI-powered explanation
   - Why it's important
   - How to learn it
   - Time required
   - Free certification resources

### AI Mentor Chat

1. Click on "AI Mentor" in the navigation
2. Ask questions about learning paths, career advice, or specific topics
3. Get personalized responses from the AI mentor

## API Endpoints

### GET /
- Health check endpoint
- Returns: `{"status": "Backend Running 🚀"}`

### GET /skills
- Get list of available skills
- Returns: Array of skill names

### POST /generate
- Generate roadmap for a skill
- Body: `{"skill": "python"}`
- Returns: `{"roadmap": {"nodes": [...], "edges": [...]}}`

### POST /explain
- Get AI explanation for a topic
- Body: `{"topic": "Machine Learning"}`
- Returns: `{"explanation": "..."}`

### POST /node-certs
- Get certification recommendations
- Body: `{"node": "Python Basics"}`
- Returns: `{"certifications": [...]}`

### POST /chat
- Chat with AI mentor
- Body: `{"question": "How do I learn React?"}`
- Returns: `{"reply": "..."}`

## Customization

### Adding New Roadmaps

Edit `backend/roadmaps_master.json` and add new skills with their nodes and edges:

```json
{
  "your-skill": {
    "nodes": ["Topic 1", "Topic 2", "Topic 3"],
    "edges": [
      ["Topic 1", "Topic 2"],
      ["Topic 2", "Topic 3"]
    ]
  }
}
```

### Changing the AI Model

In `backend/app.py`, update the `ask_openrouter` function to use a different model:

```python
payload = {
    "model": "anthropic/claude-3-sonnet",  # Change this
    "messages": messages
}
```

## Deployment

### Backend Deployment (Heroku)

1. Create a `Procfile`:
```
web: cd backend && gunicorn app:app
```

2. Add `gunicorn` to `requirements.txt`

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Frontend Deployment (Netlify/Vercel)

1. Update `API_BASE` in `frontend/app.js` to your deployed backend URL
2. Deploy the `frontend` folder to Netlify or Vercel

### Environment Variables

For production, set the `OPENROUTER_API_KEY` as an environment variable instead of hardcoding it:

```python
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
```

## License

MIT License

## Support

For issues and questions, please open an issue on the project repository.
