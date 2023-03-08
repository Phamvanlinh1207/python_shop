from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from model_utils.fields import StatusField
from model_utils import Choices
import random
import string
import secrets
# Create your models here.
# model category
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, max_length=1208)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.title

# model Product
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
    @staticmethod
    def get_all_product_py_id(Category):
        if Category:
            return Product.objects.filter(Category = Category)
        else:
            return Product.objects.all()
# model order
class Order(models.Model):
    code = get_random_string(length=5, allowed_chars='CCCAAAAGTACGTCCGGCATTTGTCCACCCCT').lower()
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='orders')
    STATUS = Choices('Order','trade', 'published','end','Canceled')
    status = StatusField()
    is_paid = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def get_cart_total(self):
        order_detail = self.order_detail.all()
        price = []
        for order_detail in order_detail:
            price.append(order_detail.product.price)
        return sum(price)

    def __str__(self):
        return self.code
# model orderDetail
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True,default=0)

    def get_product_price(self):
        price = [self.product.price * self.product.quantity]
        return sum(price)

