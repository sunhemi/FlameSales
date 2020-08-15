from django.contrib import admin
from .models import Deal, Category, Tag, Store, StoreImage
# Register your models here.

#### Actions ####
# publish multipy deals 
def make_published(modeladmin,request,queryset):
    queryset.update(is_draft='publish')

## change Feature
def make_huo_only(modeladmin,request,queryset):
    queryset.update(feature='HuoOnly')

def make_hot_deals(modeladmin,request,queryset):
    queryset.update(feature='HotDeals')

def make_good_deals(modeladmin,request,queryset):
    queryset.update(feature='GoodDeals')

    
# change action name 
make_published.short_description = "Mark Deals as Published "
make_huo_only.short_description = "Mark Deals as Huo Only "
make_hot_deals.short_description = "Mark Deals as Hot Deals "
make_good_deals.short_description = "Mark Deals as Good Deals "


#### UI ####

# Deal 
@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    # show options 
    list_display = ('id','title','is_active','content','publish_time','expire_date','not_delated')
    # Orders 
    ordering = ('not_delated','-is_active','updated_time')
    actions = [make_published,make_good_deals,make_hot_deals,make_huo_only,]


# Store Image Admin 
# class StoreImageInline(admin.TabularInline):
#      model = StoreImage
    
    # def get_extra(self, request, obj=None, **kwargs):
        # extra = 2
        # if obj:
            # # return extra - obj.binarytree_set.count()
        # return extra

# class StoreAdmin(admin.ModelAdmin):
#     inlines = [StoreImageInline, ]

admin.site.register([Category,Tag,Store])
# Store,StoreImageInline


