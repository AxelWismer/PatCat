"""PatCat URL Configuration"""

from django.contrib import admin
from django.urls import path
from patterns.views import search
from .memory_db import set_memory_db

# Set the in-memory database from the persistent database
set_memory_db()
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search, name='search')
]
