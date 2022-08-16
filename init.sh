# USE FOR DEVELOPMENT ONLY

# rm old migrations and db 
rm patterns/migrations/0001_initial.py
rm memory_DB/migrations/0001_initial.py
rm db.sqlite3

# Set the initial files
rm -R media/
cp -r test_data/ media/
cp patterns/inital_data/db.json media/db/db.json

# Aply migrations and store a copy of the db
python manage.py makemigrations
python manage.py migrate
cp db.sqlite3 initial_db.sqlite3
mkdir media/db

# Create the documentation
python manage.py graph_models -o docs/patterns_models.png

# Run the aplication
python manage.py runserver