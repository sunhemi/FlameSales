from django.contrib import admin
from .models import Deal, Category, Tag, Store, Feature
# Register your models here.

admin.site.register([Deal,Category,Tag,Store,Feature])
