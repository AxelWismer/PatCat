rm patterns/migrations/0001_initial.py
rm db.sqlite3
rm -R media/
cp -r test_data/ media/

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata patterns/inital_data/*
python manage.py graph_models -o docs/patterns_models.png
python manage.py runserver