#!/bin/bash -xe

DATABASE_HOST = $1
echo "Waiting for database"

while ! nc -zv $DATABASE_HOST 5432; do
    sleep 1
done

echo "Database initialised"

python manage.py run -h 0.0.0.0