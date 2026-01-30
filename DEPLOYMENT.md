# Politics Backend - Deployment Guide

## ✅ Current Status
- **Local Development**: ✅ Working
- **API Endpoints**: ✅ Functional
- **Database**: ✅ SQLite (local)
- **Ready for Production**: ✅ Yes

## 🚀 Render Deployment (Recommended)

1. Push code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New+" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - Name: `politics-backend`
   - Runtime: Python 3
   - Build Command: `pip install -r politics_backend/requirements.txt`
   - Start Command: `bash start.sh`
6. Add Environment Variables:
   - `SECRET_KEY` (auto-generated or custom)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: your-domain.onrender.com
   - `CORS_ALLOW_ALL_ORIGINS`: `True`
7. Click "Create Web Service"

## Docker Deployment

### Local Development
```bash
docker-compose up --build
```

### Production Build
```bash
docker build -t politics-backend .
docker run -p 8000:8000 politics-backend
```

## 🔧 Required Environment Variables

**Mandatory for Production**:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to `False`
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - PostgreSQL connection string (Render auto-provides this)
- `CORS_ALLOW_ALL_ORIGINS` - Set to `True` for development

## 💻 Local Development Setup

1. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r politics_backend/requirements.txt
```

3. Run migrations:
```bash
python politics_backend/manage.py migrate
```

4. Create superuser:
```bash
python politics_backend/manage.py createsuperuser
```

5. **Run development server**:
```bash
python politics_backend/manage.py runserver
```