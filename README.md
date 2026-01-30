# Politics Backend

PostgreSQL + Session-based Authentication Django REST API

## Database Connection

**Database**: `politics_backend` (PostgreSQL)
**Host**: `localhost`
**Port**: `5432`
**Username**: `manibharadwaj`
**Password**: *(empty)*

## Environment Variables

See `.env` file for configuration:
- `DB_NAME=politics_backend`
- `DB_USER=manibharadwaj`
- `DB_PASSWORD=`
- `DB_HOST=localhost`
- `DB_PORT=5432`

## Key Features

- ✅ PostgreSQL database
- ✅ Session-based authentication (no JWT)
- ✅ User approval workflow
- ✅ Admin-only endpoints
- ✅ Production-ready

## API Endpoints

- `POST /api/register/` - User registration
- `POST /api/login/` - User login (session-based)
- `GET /api/profile/` - User profile
- `GET /api/pending-users/` - Admin: View pending users
- `POST /api/approve-user/<id>/` - Admin: Approve users
- `GET /api/protected/` - Public endpoint

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Start server: `python manage.py runserver`
4. Access API at: `http://127.0.0.1:8000`# politics_backend
# politics_backend
# politics_backend
# docker_politics_backend
# docker_politics_backend
# docker_politics_backend
