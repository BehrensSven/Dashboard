#!/bin/sh
set -e

python manage.py makemigration

# Führe Datenbankmigrationen durch
python manage.py migrate --noinput

# Lade die vorgefertigten Daten
python manage.py loaddata fixtures/initial_data.json

# Starte den Django-Entwicklungsserver
exec python manage.py runserver 0.0.0.0:8000
