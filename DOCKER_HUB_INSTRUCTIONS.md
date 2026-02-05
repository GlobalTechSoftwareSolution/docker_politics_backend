# Docker Hub Deployment Instructions

## Prerequisites

1. Make sure you have Docker installed and running
2. Create an account on [Docker Hub](https://hub.docker.com/) if you don't have one
3. Log in to Docker Hub from your terminal: `docker login`

## Pushing the Image to Docker Hub

### Option 1: Using the automated script

Run the provided script:
```bash
./build_push_docker.sh
```

The script will:
1. Prompt you for your Docker Hub username
2. Build the Docker image
3. Tag it with your username
4. Push it to Docker Hub

### Option 2: Manual process

1. Build the image:
```bash
docker build -t politics_backend .
```

2. Tag the image with your Docker Hub username:
```bash
docker tag politics_backend your-dockerhub-username/politics_backend:latest
```

3. Push the image:
```bash
docker push your-dockerhub-username/politics_backend:latest
```

## Running the Image from Docker Hub

### Direct run:
```bash
docker run -p 8003:8003 your-dockerhub-username/politics_backend:latest
```

### Using docker-compose:

Update your docker-compose file to use the image instead of building locally:

```yaml
version: '3.8'

services:
  backend:
    image: your-dockerhub-username/politics_backend:latest
    ports:
      - "8003:8003"
    environment:
      - DEBUG=True
      - DATABASE_URL=postgresql://neondb_owner:npg_gYkWjL83AUhb@ep-weathered-feather-ah46b9c8.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require
      - SECRET_KEY=django-insecure-sh4ggvb1i2x$n5cyzfj7#sndw%8hfd(()e%i)i!&x%7gezm3j6
    volumes:
      - .:/app
    working_dir: /app/politics_backend
    command: sh -c "python manage.py migrate --settings=politics_backend.local_settings && gunicorn --bind 0.0.0.0:8003 politics_backend.wsgi:application"
```

Then run:
```bash
docker-compose up
```

## Cloning and Running the Project

To clone and run this project from anywhere:

1. Clone the repository:
```bash
git clone <your-repo-url>
cd politics/politics_backend
```

2. Pull and run the Docker image from Docker Hub:
```bash
docker pull your-dockerhub-username/politics_backend:latest
docker run -p 8003:8003 your-dockerhub-username/politics_backend:latest
```

Or use the docker-compose approach described above with the image instead of building locally.

## Notes

- The application runs on port 8003 inside the container
- Make sure your environment variables are properly configured
- The database migration will run automatically when the container starts