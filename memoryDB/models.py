from django.db import models
from django.core.files.storage import get_storage_class

# Create your models here.
INTERMEDIATE_DB_URL = "memoryDB/intermediate_db.json"
DB_CONFIGURATION = "memoryDB/db_configuration.json"
DB_URL = "db/db.json"

# Custom data storage that always keeps the same name for a file
class ConstantNamesStorage(get_storage_class()):
    def _save(self, name, content):
        self.delete(name)
        return super(ConstantNamesStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name
    
def structure_path(instance, filename):
    return DB_URL

class Config(models.Model):
    db = models.FileField(upload_to=structure_path, verbose_name="Database", storage=ConstantNamesStorage())
    
    def __str__(self): return f'{self.db} ({self.pk})'
    