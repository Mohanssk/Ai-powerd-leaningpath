# Installation Guide

Complete installation instructions for SkillPath.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **RAM**: 512 MB minimum
- **Disk Space**: 100 MB for application and dependencies
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

### Recommended Requirements
- **Python**: 3.11 or higher
- **RAM**: 1 GB or more
- **Internet**: Stable connection for AI features

## Installation Methods

### Method 1: Quick Install (Recommended)

#### Step 1: Clone or Download Project
```bash
cd /path/to/your/projects
```

If using Git:
```bash
git clone <repository-url>
cd project
```

Or download and extract the ZIP file.

#### Step 2: Install Backend
```bash
cd backend
pip install -r requirements.txt
```

#### Step 3: Start Backend
```bash
python app.py
```

Leave this terminal open. You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

#### Step 4: Open Frontend
Open a new terminal:
```bash
cd frontend
python -m http.server 8000
```

#### Step 5: Access Application
Open browser: `http://localhost:8000`

### Method 2: Using Startup Script

#### Linux/macOS
```bash
chmod +x start.sh
./start.sh
```

#### Windows
Create `start.bat`:
```batch
@echo off
cd backend
pip install -r requirements.txt
start python app.py
cd ../frontend
start python -m http.server 8000
echo Frontend: http://localhost:8000
pause
```

Run:
```batch
start.bat
```

### Method 3: Docker Installation

#### Prerequisites
- Docker Desktop installed
- Docker Compose installed

#### Steps
```bash
docker-compose up
```

Access at: `http://localhost:8080`

To stop:
```bash
docker-compose down
```

### Method 4: Virtual Environment (Best Practice)

#### Linux/macOS
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

#### Windows
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

To deactivate:
```bash
deactivate
```

## Platform-Specific Instructions

### Windows

#### Install Python
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. Check "Add Python to PATH"
4. Click "Install Now"

#### Verify Installation
```bash
python --version
pip --version
```

#### Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Run Backend
```bash
python app.py
```

#### Run Frontend
Open `frontend/index.html` directly in browser or:
```bash
cd frontend
python -m http.server 8000
```

### macOS

#### Install Python (using Homebrew)
```bash
brew install python@3.11
```

#### Verify Installation
```bash
python3 --version
pip3 --version
```

#### Install Dependencies
```bash
cd backend
pip3 install -r requirements.txt
```

#### Run Application
```bash
python3 app.py
```

### Linux (Ubuntu/Debian)

#### Install Python
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Verify Installation
```bash
python3 --version
pip3 --version
```

#### Install Dependencies
```bash
cd backend
pip3 install -r requirements.txt
```

#### Run Application
```bash
python3 app.py
```

## Troubleshooting Installation

### Python Not Found

**Windows:**
```bash
py --version
```
Use `py` instead of `python`

**macOS/Linux:**
```bash
python3 --version
```
Use `python3` instead of `python`

### Pip Not Found

**Install pip:**
```bash
python -m ensurepip --upgrade
```

Or:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Permission Denied

**Linux/macOS:**
```bash
sudo pip install -r requirements.txt
```

Or use virtual environment (recommended)

### Port Already in Use

**Backend (Port 5000):**
Change in `app.py`:
```python
app.run(debug=True, port=5001)
```

Update in `frontend/app.js`:
```javascript
const API_BASE = 'http://localhost:5001';
```

**Frontend (Port 8000):**
```bash
python -m http.server 8080
```

### Module Not Found Error

**Solution 1:** Reinstall dependencies
```bash
pip install -r requirements.txt --force-reinstall
```

**Solution 2:** Use virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### SSL Certificate Error

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Version Conflicts

**Create fresh virtual environment:**
```bash
python -m venv fresh_env
source fresh_env/bin/activate
pip install -r requirements.txt
```

## Configuration

### Environment Variables

#### Create .env file
```bash
cp .env.example .env
```

#### Edit .env
```
OPENROUTER_API_KEY=your_actual_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

#### Load in Python
Add to `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
```

Install python-dotenv:
```bash
pip install python-dotenv
```

### Custom Configuration

#### Change Backend Port
In `backend/app.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
```

#### Change Frontend API URL
In `frontend/app.js`:
```javascript
const API_BASE = 'http://localhost:5000';
```

## Verification

### Test Backend
```bash
cd project
python test_backend.py
```

Expected output:
```
Health Check: PASSED
Skills Endpoint: PASSED
Roadmap Generation: PASSED
Node Certifications: PASSED

Total: 4/4 tests passed
```

### Test Frontend
1. Open `http://localhost:8000`
2. Enter "Python" in skill field
3. Click "Generate"
4. Verify roadmap appears
5. Click a node to see details

### Check Logs

**Backend Logs:**
- Should show requests and responses
- No error messages
- Status 200 for successful requests

**Browser Console:**
- Open with F12
- No red error messages
- Network tab shows 200 status

## Post-Installation

### Update Project
```bash
git pull origin main
cd backend
pip install -r requirements.txt --upgrade
```

### Add to Startup (Optional)

**Linux:**
Create systemd service or add to crontab

**macOS:**
Create LaunchAgent

**Windows:**
Add to Task Scheduler

## Getting Help

### Check Documentation
- README.md - Overview
- QUICKSTART.md - Quick start
- FEATURES.md - Feature list
- DEPLOYMENT.md - Production deployment

### Common Issues
- Python version too old → Upgrade to 3.8+
- Port conflicts → Change ports
- Dependencies fail → Use virtual environment
- CORS errors → Check backend is running

### Support Resources
- Project documentation
- GitHub issues
- Stack Overflow
- Python documentation

## Next Steps

After installation:
1. Read QUICKSTART.md for usage
2. Try generating different roadmaps
3. Explore AI features
4. Customize roadmaps in JSON file
5. Consider deployment options

## Uninstallation

### Remove Virtual Environment
```bash
rm -rf venv  # Linux/macOS
rmdir /s venv  # Windows
```

### Remove Project
```bash
cd ..
rm -rf project
```

### Remove Python Packages
```bash
pip uninstall -y Flask Flask-CORS requests gunicorn
```

---

Installation complete! Proceed to QUICKSTART.md for usage instructions.
