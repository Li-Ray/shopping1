from django.contrib import admin
from products.models import Product, ProductImages, Order, SlideShow

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Order)
admin.site.register(SlideShow)