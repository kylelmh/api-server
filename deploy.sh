#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn app.asgi -k uvicorn.workers.UvicornWorker 