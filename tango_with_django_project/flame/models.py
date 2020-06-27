from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# Category Model
class Category(models.Model):
    name = models.CharField(max_length = 50)
    class Meta:
            verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

# Tag Model 
class Tag(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

# pick from Hot Deals / Huo-Only Deals / Normal Deals 

# class Feature(models.Model):
#    name = models.CharField(max_length = 12) 
#    # option = feature_option[2]
#    def __str__(self):
#        return self.name

class Store(models.Model):
    #store information 
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100,blank=True)
    websites = models.URLField(blank=True)
    # phone number field - may change to a better one
    phone = models.CharField(max_length = 10, blank=True)
    wechat = models.CharField(max_length = 30, blank = True) 

    def __str__(self):
        return self.name 

# Add a post status 


class Deal(models.Model):
    STATUS = (
    ('draft', "Draft"),
    ('publish',"Publish")
    )

    FEATURE = (
    ('HotDeals', 'Hot Deals'),
    ('HuoOnly', 'Huozhezi Only'),
    ('Trending', 'Trending Deals'),
    ('GoodDeals','Good Deals'),
    )

    # Basic Properties 
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200)

    ###############!!! NEED TO ADD IMAGE TOO 
    content = models.TextField() 
    author = models.ForeignKey(User,on_delete= models.CASCADE,related_name='blog_posts')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    publish_time = models.DateTimeField(default=timezone.now)
    not_delated = models.BooleanField(default = True)
    is_draft = models.CharField(max_length=10, choices=STATUS, default='publish')
    feature = models.CharField(max_length=10,choices = FEATURE, default='GoodDeals')    

    
    # Customized Properties 
    effective_date = models.DateField()
    expire_date = models.DateField()
    is_active = models.BooleanField(default=True)

    old_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0)
    new_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0)
    #save = "{:.0f}".format((new_price - old_price)/old_price)

    # Save Deal Information 
    store = models.ForeignKey(Store, on_delete=models.CASCADE,related_name="store",null = True)
        #url info: if there is a link: putlink 
        # o/w put deal itself default link
    url = models.URLField(blank=True)

    # views = models.IntegerField(max_length = 2)
    # likes = models.IntergerField(max_length = 2)

    class Meta:
        ordering = ('-publish_time',)

    def __str__(self):
        return self.title


