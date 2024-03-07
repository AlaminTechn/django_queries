#!/bin/sh

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --noinput

# Start the Django application
gunicorn advanced_queries.wsgi:application -b 0.0.0.0:8001