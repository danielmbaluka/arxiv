#!/usr/bin/env bash

echo "Running python manage.py migrate ..."
python manage.py migrate --noinput --settings=$DJANGO_SETTINGS_MODULE

echo "Installing seed data from fixtures ..."
python manage.py loaddata topics

echo "Starting application on 0.0.0.0:8001 ..."

python manage.py runserver 0.0.0.0:8001
