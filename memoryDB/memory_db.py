from django.core.management import call_command
from django.conf import settings
import shutil
import os
from django.core.files import File
from .models import * 
from patterns.models import *
from django.core.files.storage import default_storage

DB_READY = False
# Configure the database in memory for a single time at the beginning of the application
def set_memory_db():
    # Commands to run at startup
    if not settings.RUNNING_DB_COMMANDS:
        # Start with an empty database with migrations to save time
        if not os.path.exists(settings.TMP_DIR + '/db.json'):
            shutil.copyfile('patterns/inital_data/db.json', settings.TMP_DIR + '/db.json')
        shutil.copyfile('initial_db.sqlite3', settings.TMP_DIR + '/db.sqlite3')
        # Load the information from the configuration file in json format
        call_command('loaddata', DB_CONFIGURATION)
        
        # Get the DB file and store it in a intermidiate file in memory
        config_data = default_storage.open(DB_URL).read()
        with open(INTERMEDIATE_DB_URL, 'w') as f:
            myfile = File(f)
            myfile.write(config_data.decode())

        # Load the intermidiate file into the db and remove it
        call_command('loaddata', INTERMEDIATE_DB_URL)
        os.remove(INTERMEDIATE_DB_URL)
        
    from .post_save_handler import post_save_handler