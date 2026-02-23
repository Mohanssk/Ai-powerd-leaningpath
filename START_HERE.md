# START HERE

Welcome to SkillPath! This guide will get you up and running in minutes.

## What is SkillPath?

An AI-powered learning roadmap generator that creates personalized learning paths with:
- Visual roadmaps for technical skills
- AI-powered explanations
- Free certification recommendations
- Interactive AI mentor

## Fastest Way to Start

### Option 1: Direct Open (Instant)
1. Open `frontend/index.html` in your browser
2. Type a skill (e.g., "Python")
3. Click "Generate"

**Note**: Backend features (AI explanations, chat) won't work without running the server.

### Option 2: Full Setup (5 minutes)

#### Step 1: Start Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

Keep this terminal open.

#### Step 2: Start Frontend
Open a new terminal:
```bash
cd frontend
python -m http.server 8000
```

#### Step 3: Use the App
Open browser: http://localhost:8000

### Option 3: Docker (2 minutes)
```bash
docker-compose up
```
Open browser: http://localhost:8080

## What Can You Do?

1. **Generate Roadmaps**: Enter any skill to see a learning path
2. **Explore Topics**: Click nodes to get AI explanations
3. **Find Resources**: Get free certification links
4. **Ask Questions**: Chat with AI mentor

## Included Skills

- Python (22 topics)
- JavaScript (21 topics)
- Web Development (20 topics)
- Data Science (20 topics)

## Documentation

- **QUICKSTART.md** - Quick setup guide
- **README.md** - Full documentation
- **FEATURES.md** - Feature list
- **DEPLOYMENT.md** - Deploy to production
- **TREE.txt** - Visual project structure

## Need Help?

1. Check QUICKSTART.md for detailed setup
2. Review INSTALL.md for troubleshooting
3. See README.md for full documentation

## What's Next?

- Customize roadmaps in `backend/roadmaps_master.json`
- Deploy to production (see DEPLOYMENT.md)
- Add your own skills and topics

---

Ready? Open `frontend/index.html` or run the commands above!
