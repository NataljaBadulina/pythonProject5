from django.contrib import admin
from .models import Category, Product, Staff, Order, ProductOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Order)
admin.site.register(ProductOrder)
