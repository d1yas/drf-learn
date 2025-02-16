#!/bin/bash

if [ -d "venv" ]; then
    source venv/bin/activate
    echo "Virtual muhit aktivlashtirildi"
fi

if [ -d "UserApp/migrations" ]; then
    rm -rf UserApp/migrations/*
    echo "Usersapp migrations tozalandi"
fi


touch UserApp/migrations/__init__.py
echo "Yangi __init__.py fayllari yaratildi"

python manage.py collectstatic --noinput

python manage.py makemigrations UserApp
python manage.py migrate
python manage.py createsuperuser