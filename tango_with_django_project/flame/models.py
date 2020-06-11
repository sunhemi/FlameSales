from django.db import models
from django.contrib.auth.models import User

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
feature_option = (
    'Hot Deals',
    'Huo Only Deals',
    'Normal Deals'
)

class Feature(models.Model):
    name = models.CharField(max_length = 12) 
    option = feature_option[2]
    def __str__(self):
        return name

# Add a post status 
STATUS = (
    (0, "Draft"),
    (1,"Publish")
)

class Deal(models.Model):
    # Basic Properties 
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200)
    content = models.TextField() 
    author = models.ForeignKey(User,on_delete= models.CASCADE,related_name='blog_posts')
    created_time = models.DateTimeField(auto_now_add=True)
    publish_time = models.DateTimeField(auto_now=True)
    
    # Customized Properties 
    effective_date = models.DateField()
    expire_date = models.DateField()
    is_active = models.BooleanField()


    def __str__(self):
        return self.title

