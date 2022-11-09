# USE FOR DEVELOPMENT ONLY

# rm old migrations and db 
rm patterns/migrations/0001_initial.py
rm memory_DB/migrations/0001_initial.py
rm tmp/db.sqlite3

# Set the initial files
rm -R tmp/media/
cp -r test_data/ tmp/media/
mkdir media/db
cp patterns/inital_data/db.json tmp/db.json

# Aply migrations and store a copy of the db
python manage.py makemigrations
python manage.py migrate
cp db.sqlite3 initial_db.sqlite3

# Create the documentation
python manage.py graph_models -o docs/patterns_models.png
python manage.py graph_models memoryDB -o docs/memoryDB.png

# Run the aplication
python manage.py runserver