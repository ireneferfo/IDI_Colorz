#!/bin/sh

rm vg_app/migrations/0001_initial.py
rm -r vg_app/migrations/__pycache__
rm db.sqlite3

python manage.py makemigrations vg_app
python manage.py migrate
python manage.py sqlmigrate vg_app 0001 