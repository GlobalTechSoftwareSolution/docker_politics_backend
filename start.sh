#!/bin/bash

# Wait for database to be ready
sleep 5

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

# Start the server
exec gunicorn politics_backend.wsgi:application --bind 0.0.0.0:$PORT --workers 3