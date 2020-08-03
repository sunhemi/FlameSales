from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt

# Create your models here.

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# def get_image_filename(instance, filename):
#     title = instance.post.title
#     slug = slugify(title)
#     return "post_images/%s-%s" % (slug, filename)  

# Create a Store 
class Store(models.Model):
    # store information
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    websites = models.URLField(blank=True)
    # phone number field - may change to a better one
    phone = models.CharField(max_length=10, blank=True)
    wechat = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class StoreImage(models.Model):
    store = models.ForeignKey(Store,on_delete = models.CASCADE ,related_name='storeimages')
    image = models.ImageField()


# # Multiply Image 
# class DealImage(models.Model):
#     deal = models.ForeignKey(Deal,default=None)
#     image = models.ImageField(upload_to = get_image_filename, verbose_name='Deal Image')

# Create a deal 
class Deal(models.Model):
    STATUS = (
        ('draft', "Draft"),
        ('publish', "Publish")
    )

    FEATURE = (
        ('HotDeals', 'Hot Deals'),
        ('HuoOnly', 'Huozhezi Only'),
        #('Trending', 'Trending Deals'),
        ('GoodDeals', 'Good Deals'),
    )

    # Basic Properties
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    tag = models.ManyToManyField(Tag)
    content = models.TextField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    publish_time = models.DateTimeField(default=timezone.now)
    not_delated = models.BooleanField(default=True)
    is_draft = models.CharField(
        max_length=10, choices=STATUS, default='publish')
    feature = models.CharField(
        max_length=10, choices=FEATURE, default='GoodDeals')

    # Customized Properties
    effective_date = models.DateField()
    expire_date = models.DateField()
    
    is_active = models.BooleanField(default=True)

    old_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0)
    new_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0)
    #save = "{:.0f}".format((new_price - old_price)/old_price)

    # Save Deal Information
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="store", null=True)
    # url info: if there is a link: putlink
    # o/w put deal itself default link
    url = models.URLField(blank=True)
    # views = models.IntegerField(max_length = 2)
    # likes = models.IntergerField(max_length = 2)

    class Meta:
        ordering = ('-publish_time',)

    def __str__(self):
        return self.title