# SkillPath Features

## Core Features

### 1. Interactive Learning Roadmaps

Generate personalized learning paths for various technical skills:

- **Visual Path Structure**: See your learning journey laid out in an intuitive, numbered sequence
- **Multiple Skills**: Pre-configured roadmaps for Python, JavaScript, Web Development, and Data Science
- **Expandable System**: Easy to add new skills and customize learning paths
- **Progressive Learning**: Each node builds upon previous knowledge

### 2. AI-Powered Explanations

Get intelligent insights for every learning topic:

- **What It Is**: Clear definition and overview of the concept
- **Why It's Important**: Understanding the value and relevance
- **How to Learn**: Practical guidance and learning strategies
- **Time Required**: Realistic time estimates for mastering each topic

Powered by OpenRouter API with GPT-3.5 Turbo.

### 3. Free Certification Engine

Automatically curated learning resources for every topic:

- **freeCodeCamp**: Interactive coding tutorials
- **Coursera**: University-level courses
- **edX**: Professional certificates
- **Google Digital Garage**: Industry certifications
- **Kaggle Learn**: Data science and ML courses

All resources are completely free!

### 4. AI Learning Mentor

Interactive chat interface for personalized guidance:

- **Career Advice**: Get insights on learning paths and career transitions
- **Topic Explanations**: Ask questions about specific technologies
- **Learning Strategies**: Receive personalized study recommendations
- **Real-time Responses**: Powered by advanced AI models

### 5. Modern, Responsive UI

Beautiful interface built with modern web technologies:

- **Tailwind CSS**: Clean, professional design
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Smooth Animations**: Engaging hover effects and transitions
- **Intuitive Navigation**: Easy to use for all skill levels
- **Modal Dialogs**: Focused view for detailed information

## Technical Features

### Backend (Python + Flask)

- **RESTful API**: Clean, documented endpoints
- **CORS Support**: Easy frontend integration
- **Error Handling**: Robust error management
- **Modular Design**: Easy to extend and maintain
- **JSON Data Store**: Simple, portable data format

### Frontend (HTML + Tailwind + JavaScript)

- **Vanilla JavaScript**: No complex frameworks required
- **CDN-based Tailwind**: Zero build process
- **Async/Await**: Modern JavaScript patterns
- **Event-driven**: Responsive user interactions
- **Local Storage Ready**: Can cache data for offline use

### API Endpoints

1. **GET /**: Health check
2. **GET /skills**: List available skills
3. **POST /generate**: Generate roadmap
4. **POST /explain**: AI topic explanation
5. **POST /node-certs**: Get certifications
6. **POST /chat**: AI mentor chat

### Data Structure

Roadmaps are stored as graph structures:

```json
{
  "skill-name": {
    "nodes": ["Topic 1", "Topic 2", "Topic 3"],
    "edges": [
      ["Topic 1", "Topic 2"],
      ["Topic 2", "Topic 3"]
    ]
  }
}
```

This allows for:
- Linear learning paths
- Branching paths
- Prerequisites visualization
- Flexible roadmap design

## Use Cases

### For Learners

- **Career Switchers**: Structured path for transitioning to tech
- **Students**: Supplement formal education with practical guidance
- **Self-taught Developers**: Organized approach to learning
- **Skill Upgraders**: Structured way to learn new technologies

### For Educators

- **Curriculum Planning**: Use roadmaps as course structure
- **Resource Curation**: Leverage free certification links
- **Progress Tracking**: Visual representation of learning journey
- **Student Guidance**: AI mentor for student questions

### For Organizations

- **Onboarding**: Training paths for new hires
- **Skill Development**: Employee upskilling programs
- **Team Training**: Consistent learning standards
- **Career Ladders**: Clear skill progression paths

## Customization Options

### Add New Roadmaps

Edit `backend/roadmaps_master.json`:

```json
{
  "your-skill": {
    "nodes": ["Beginner Topic", "Intermediate Topic", "Advanced Topic"],
    "edges": [
      ["Beginner Topic", "Intermediate Topic"],
      ["Intermediate Topic", "Advanced Topic"]
    ]
  }
}
```

### Change AI Model

In `backend/app.py`:

```python
payload = {
    "model": "anthropic/claude-3-sonnet",  # or any OpenRouter model
    "messages": messages
}
```

### Customize UI Colors

In `frontend/index.html`, update Tailwind classes:

- Change `blue` to `purple`, `green`, `red`, etc.
- Modify gradient classes: `from-blue-50` to `from-purple-50`
- Update button colors: `bg-blue-600` to `bg-green-600`

### Add More Certification Sources

In `backend/app.py`, update `generate_free_certs()`:

```python
{
    "title": f"Your Platform - {topic}",
    "url": f"https://yourplatform.com/search?q={q}"
}
```

## Planned Features (Roadmap)

- User authentication and progress tracking
- Save and resume learning paths
- Community-contributed roadmaps
- Learning time estimates per node
- Prerequisite checking
- Completion tracking
- Achievement badges
- Social sharing
- Mobile app version
- Offline mode
- Multi-language support
- Video resource integration
- Practice exercises
- Quiz generation
- Peer learning groups

## Performance

- **Fast Load Times**: Minimal dependencies
- **Efficient API**: Cached responses where possible
- **Lightweight Frontend**: No heavy frameworks
- **Scalable Backend**: Easy to add workers
- **Low Resource Usage**: Runs on minimal hardware

## Security

- **CORS Protected**: Configurable origin restrictions
- **Input Validation**: Sanitized user inputs
- **No User Data Storage**: Privacy-focused design
- **API Key Security**: Environment variable support
- **Rate Limiting Ready**: Easy to add rate limits

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Opera 76+

## Accessibility

- Semantic HTML
- Keyboard navigation support
- Screen reader friendly
- High contrast support
- Responsive text sizing

## License

MIT License - Free for personal and commercial use
