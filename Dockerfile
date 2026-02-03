FROM python:3.10-slim

WORKDIR /app/politics_backend

# Install system dependencies for testing
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY politics_backend/requirements.txt .
RUN pip install --no-cache-dir Pillow \
&& pip install --no-cache-dir -r requirements.txt

COPY . /app



EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --settings=politics_backend.local_settings && gunicorn --bind 0.0.0.0:8000 politics_backend.wsgi:application"]