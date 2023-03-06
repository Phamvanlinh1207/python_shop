from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, max_length=1208)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=False, blank=True, upload_to='photos')
    price = models.FloatField(null=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=False, max_length=1208)
    views = models.IntegerField(null=True,default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)

    def admin_photo(self):
        return mark_safe('<img src="{}" width=100px;height=150px />'.format(self.image.url))
    admin_photo.short_description = 'image'
    admin_photo.allow_tags = True
    def __str__(self):
        return self.name
