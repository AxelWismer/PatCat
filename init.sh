rm patterns/migrations/0001_initial.py
rm db.sqlite3

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata patterns/inital_data/*
python manage.py runserver