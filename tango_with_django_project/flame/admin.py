from django.contrib import admin
from .models import Deal, Category, Tag, Store
# Register your models here.

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_active','content','publish_time','expire_date','not_delated')
    ordering = ('not_delated','-is_active','updated_time')

admin.site.register([Category,Tag,Store])
