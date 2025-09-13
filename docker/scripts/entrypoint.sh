#!/bin/bash
set -e

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
email = "frankndagula12@gmail.com"
password = "admin123"
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email=email, password=password)
EOF
# Start Gunicorn
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --threads 2 \
    --timeout 120
