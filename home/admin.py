from django.contrib import admin
from .models import Category,Product
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_display = ("title", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "admin_photo", "price", "quantity", "description", "views", "category")

    readonly_fields = ['admin_photo']
