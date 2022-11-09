"""PatCat URL Configuration"""

from django.contrib import admin
from django.urls import path
from patterns.views import search
from memoryDB.memory_db import set_memory_db
from django.conf import settings
# Set the in-memory database from the persistent database
set_memory_db()
    
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', search, name='search')
]
