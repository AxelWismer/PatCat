from django.core.management import call_command

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import shutil
import os
def set_memory_db():
    # Commands to run at startup
    if not settings.RUNNING_DB_COMMANDS:
        # Start with an empty database with migrations to save time
        shutil.copyfile('initial_db.sqlite3', 'db.sqlite3')
        # Load the information from the persistent database in json format
        call_command('loaddata', 'db.json')
        
        # After the initial data load, any data modifications will be reflected in the db.json file
        @receiver(post_save, sender=None)
        def my_handler(sender, **kwargs):
            call_command('dumpdata', indent=2, output='db.json')
            print('post save callback')