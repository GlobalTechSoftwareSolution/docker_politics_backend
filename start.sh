#!/bin/bash

# Wait for database to be ready
sleep 10

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

# Create superuser if not exists
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@example.com').exists() or User.objects.create_superuser('admin@example.com', 'admin123')" | python manage.py shell

# Load initial data
python manage.py loaddata users_data.json || echo "No users data to load"
python manage.py loaddata pending_info_data.json || echo "No pending info data to load"
python manage.py loaddata active_info_data.json || echo "No active info data to load"

# Start the server
exec gunicorn politics_backend.wsgi:application --bind 0.0.0.0:$PORT --workers 3