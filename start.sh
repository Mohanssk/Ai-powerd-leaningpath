#!/bin/bash

echo "Starting SkillPath Application..."
echo "================================"

cd backend

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "Starting Flask backend on http://localhost:5000"
python app.py &

BACKEND_PID=$!

cd ../frontend

echo "Frontend is ready at frontend/index.html"
echo "Open frontend/index.html in your browser or serve it with:"
echo "  - Python: python -m http.server 8000"
echo "  - Node.js: npx http-server -p 8000"
echo ""
echo "Press Ctrl+C to stop the backend server"

wait $BACKEND_PID
