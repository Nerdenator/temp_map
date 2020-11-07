#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for PostgreSQL..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate --no-input

python manage.py createsuperuser --no-input --email a.mcruer@yopmail.com

exec "$@"