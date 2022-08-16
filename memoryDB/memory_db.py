from django.core.management import call_command
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import shutil
import os
from django.core.files import File
from .models import * 
from patterns.models import *
from django.core.files.storage import default_storage
from django.contrib.admin.models import LogEntry 

# Configure the database in memory for a single time at the beginning of the application
def set_memory_db():
    # Commands to run at startup
    if not settings.RUNNING_DB_COMMANDS:
        # Start with an empty database with migrations to save time
        shutil.copyfile('initial_db.sqlite3', 'db.sqlite3')
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
        
        # After the initial data load, any data modifications will be reflected in the db.json file
        @receiver(post_save, sender=None)
        # For all models that do not belong to the exceptions, save the data in the intermediate database 
        # and, with that file, update the database in the model config.
        def my_handler(sender, **kwargs):
            exceptions = [Config, LogEntry]
            if not any(map(lambda exception: isinstance(kwargs['instance'], exception), exceptions) ) :
                call_command('dumpdata', indent=2, output=INTERMEDIATE_DB_URL)
                config = Config.objects.get(pk=0)
                config.db.save(DB_URL, File(open(INTERMEDIATE_DB_URL, 'rb')))