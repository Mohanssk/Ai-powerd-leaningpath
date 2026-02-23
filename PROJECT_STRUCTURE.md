# SkillPath Project Structure

Complete overview of the project organization and file purposes.

## Directory Structure

```
project/
├── backend/                    # Python Flask backend
│   ├── app.py                 # Main Flask application
│   ├── sanitize.py            # Data sanitization utility
│   ├── requirements.txt       # Python dependencies
│   ├── roadmaps_master.json   # Roadmap data store
│   ├── Dockerfile             # Backend container config
│   ├── runtime.txt            # Python version for deployment
│   └── .gitignore             # Backend-specific ignore rules
│
├── frontend/                   # Vanilla JavaScript frontend
│   ├── index.html             # Main HTML file
│   └── app.js                 # Frontend JavaScript logic
│
├── src/                       # Original React template (optional)
│   ├── App.tsx                # React app component
│   ├── main.tsx               # React entry point
│   ├── index.css              # Tailwind imports
│   └── vite-env.d.ts          # Vite type definitions
│
├── docs/                      # Documentation
│   ├── README.md              # Main documentation
│   ├── QUICKSTART.md          # Quick start guide
│   ├── DEPLOYMENT.md          # Deployment instructions
│   ├── FEATURES.md            # Feature documentation
│   └── PROJECT_STRUCTURE.md   # This file
│
├── config/                    # Configuration files
│   ├── .env.example           # Environment variables template
│   ├── docker-compose.yml     # Docker orchestration
│   ├── Procfile               # Heroku deployment config
│   └── .gitignore             # Global ignore rules
│
├── scripts/                   # Utility scripts
│   ├── start.sh               # Development startup script
│   └── test_backend.py        # Backend test suite
│
└── package files              # Project metadata
    ├── package.json           # Node.js dependencies (for React)
    ├── tsconfig.json          # TypeScript config
    ├── vite.config.ts         # Vite config
    ├── tailwind.config.js     # Tailwind CSS config
    └── LICENSE                # MIT license
```

## File Purposes

### Backend Files

#### `backend/app.py`
Main Flask application with all API endpoints:
- `/` - Health check
- `/skills` - List available skills
- `/generate` - Generate roadmap for a skill
- `/explain` - Get AI explanation for a topic
- `/node-certs` - Get certification links
- `/chat` - AI mentor chatbot

**Key Functions:**
- `normalize_skill()` - Standardize skill names
- `generate_free_certs()` - Generate certification links
- `ask_openrouter()` - Interact with AI API

#### `backend/sanitize.py`
Data cleaning utility for roadmap data:
- Removes marketing phrases
- Filters invalid nodes
- Validates edges
- Outputs clean JSON

#### `backend/requirements.txt`
Python package dependencies:
- Flask - Web framework
- Flask-CORS - Cross-origin support
- requests - HTTP library
- gunicorn - Production server

#### `backend/roadmaps_master.json`
Roadmap data structure:
```json
{
  "skill-name": {
    "nodes": ["Topic 1", "Topic 2"],
    "edges": [["Topic 1", "Topic 2"]]
  }
}
```

#### `backend/Dockerfile`
Container configuration for backend deployment

#### `backend/runtime.txt`
Specifies Python version for platform deployments

### Frontend Files

#### `frontend/index.html`
Main HTML structure:
- Navigation bar
- Roadmap generator section
- AI chat section
- Modal for node details
- Tailwind CSS via CDN

**Key Sections:**
- `#generator` - Roadmap generation interface
- `#chat` - AI mentor chat interface
- `#modal` - Popup for node details

#### `frontend/app.js`
Frontend application logic:
- API communication
- DOM manipulation
- Event handlers
- UI state management

**Key Functions:**
- `generateRoadmap()` - Fetch and display roadmap
- `displayRoadmap()` - Render roadmap nodes
- `showNodeDetails()` - Display modal with explanations
- `sendMessage()` - Handle chat interactions
- `showSection()` - Navigate between sections

### Documentation Files

#### `README.md`
Comprehensive project documentation:
- Features overview
- Tech stack
- Installation instructions
- API reference
- Usage examples

#### `QUICKSTART.md`
Fast setup guide:
- Prerequisites
- Installation steps
- Quick testing
- Troubleshooting

#### `DEPLOYMENT.md`
Production deployment guide:
- Heroku deployment
- Railway deployment
- DigitalOcean deployment
- AWS EC2 setup
- Docker deployment
- Frontend hosting options

#### `FEATURES.md`
Detailed feature documentation:
- Core features
- Technical features
- Use cases
- Customization options

### Configuration Files

#### `.env.example`
Template for environment variables:
```
OPENROUTER_API_KEY=your_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

#### `docker-compose.yml`
Multi-container Docker setup:
- Backend service
- Frontend with Nginx
- Environment configuration

#### `Procfile`
Heroku/Railway deployment config:
```
web: cd backend && gunicorn app:app
```

#### `.gitignore`
Version control ignore rules:
- Python cache files
- Environment variables
- IDE configurations
- Build artifacts

### Script Files

#### `start.sh`
Development startup script:
- Installs dependencies
- Starts backend server
- Provides frontend instructions

#### `test_backend.py`
Backend testing suite:
- Health check test
- Skills endpoint test
- Roadmap generation test
- Certification test

### React Template Files (Optional)

If you want to use React instead of vanilla JS:

#### `src/App.tsx`
React application component

#### `src/main.tsx`
React entry point

#### `package.json`
Node.js dependencies and scripts

#### `vite.config.ts`
Vite bundler configuration

## Data Flow

### Roadmap Generation
1. User enters skill in frontend
2. Frontend sends POST to `/generate`
3. Backend normalizes skill name
4. Backend fetches roadmap from JSON
5. Backend returns nodes and edges
6. Frontend renders roadmap

### Node Explanation
1. User clicks on node
2. Frontend sends POST to `/explain` and `/node-certs`
3. Backend queries OpenRouter API
4. Backend generates certification links
5. Frontend displays in modal

### AI Chat
1. User sends message
2. Frontend sends POST to `/chat`
3. Backend queries OpenRouter API
4. Backend returns AI response
5. Frontend displays in chat interface

## Technology Stack

### Backend
- **Framework**: Flask 3.0
- **Language**: Python 3.11
- **HTTP Client**: requests
- **CORS**: Flask-CORS
- **Server**: gunicorn (production)

### Frontend
- **Markup**: HTML5
- **Styling**: Tailwind CSS (CDN)
- **Language**: Vanilla JavaScript (ES6+)
- **HTTP Client**: Fetch API

### External Services
- **AI**: OpenRouter API (GPT-3.5 Turbo)
- **Certifications**: Various free platforms

### Development Tools
- **Version Control**: Git
- **Containerization**: Docker
- **Deployment**: Multiple platforms supported

## Extending the Project

### Adding New Skills

1. Edit `backend/roadmaps_master.json`
2. Add new skill object with nodes and edges
3. Restart backend

### Adding New API Endpoints

1. Add route in `backend/app.py`
2. Implement handler function
3. Update `frontend/app.js` to use new endpoint

### Customizing UI

1. Edit HTML structure in `frontend/index.html`
2. Modify Tailwind classes for styling
3. Update JavaScript in `frontend/app.js` for behavior

### Adding Database

1. Choose database (PostgreSQL, MongoDB, etc.)
2. Add ORM/driver to requirements.txt
3. Update app.py with database models
4. Modify endpoints to use database

### Adding Authentication

1. Choose auth method (JWT, sessions, OAuth)
2. Install auth library
3. Add login/register endpoints
4. Protect routes with auth middleware
5. Update frontend with auth forms

## Development Workflow

1. **Local Development**
   - Edit files in `backend/` or `frontend/`
   - Backend auto-reloads with Flask debug mode
   - Frontend changes reflect on page refresh

2. **Testing**
   - Run `python test_backend.py` for backend tests
   - Manual testing in browser for frontend

3. **Committing Changes**
   - Use meaningful commit messages
   - Test before committing
   - Update documentation if needed

4. **Deployment**
   - Choose deployment platform
   - Follow DEPLOYMENT.md guide
   - Set environment variables
   - Test production build

## Best Practices

### Code Organization
- Keep functions small and focused
- Use meaningful variable names
- Comment complex logic
- Separate concerns (data, logic, presentation)

### Security
- Never commit API keys
- Use environment variables
- Validate all inputs
- Implement rate limiting for production

### Performance
- Minimize API calls
- Cache responses where appropriate
- Optimize images and assets
- Use CDN for static files

### Maintenance
- Keep dependencies updated
- Monitor error logs
- Back up data regularly
- Document changes

## Troubleshooting

### Backend Issues
- Check Python version
- Verify dependencies installed
- Review error logs
- Check port availability

### Frontend Issues
- Clear browser cache
- Check browser console
- Verify API endpoint URLs
- Test CORS configuration

### Deployment Issues
- Check environment variables
- Verify build process
- Review platform-specific logs
- Test locally first

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [OpenRouter API](https://openrouter.ai/docs)
- [Docker Documentation](https://docs.docker.com/)
- [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Contributing

When contributing to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
6. Update documentation

## Support

For questions and support:
- Check documentation files
- Review troubleshooting sections
- Open an issue on GitHub
- Contact maintainers
