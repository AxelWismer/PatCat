from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UseCaseCategory)
admin.site.register(UseCase)
admin.site.register(PatternType)
admin.site.register(Pattern)
admin.site.register(Paper)
admin.site.register(SmartContract)