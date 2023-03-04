from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, max_length=1208)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, max_length=1208)
    views = models.IntegerField(null=True,default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
