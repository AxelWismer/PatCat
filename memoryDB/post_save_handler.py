from django.core.management import call_command
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File
from .models import * 
from patterns.models import *
from django.contrib.admin.models import LogEntry
from time import time

# After the initial data load, any data modifications will be reflected in the db.json file
# For all models that do not belong to the exceptions, save the data in the intermediate database 
# and, with that file, update the database in the model config.
@receiver(post_save, sender=None)
def post_save_handler(sender, **kwargs):
    # Skiping the db initialization
    if True:
        exceptions = [Config, LogEntry]
        if not any(map(lambda exception: isinstance(kwargs['instance'], exception), exceptions) ) :
            call_command('dumpdata', indent=2, output=INTERMEDIATE_DB_URL)
            config = Config.objects.get(pk=0)
            config.db.save(DB_URL, File(open(INTERMEDIATE_DB_URL, 'rb')))