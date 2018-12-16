#!/bin/sh
source venv/bin/activate

echo Starting Gunicorn.
exec gunicorn mysite.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3


#exec gunicorn -b :5000 --access-logfile - --error-logfile - mplab:app
