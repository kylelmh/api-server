#!/bin/bash

docker-compose exec api python manage.py migrate server zero
rm server/migrations/0*
docker-compose exec api python manage.py makemigrations
docker-compose exec api python manage.py migrate
