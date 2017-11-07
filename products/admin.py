from django.contrib import admin
from products.models import Product, ProductImages, Order, SlideShow


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'cellphone', 'email', 'address', 'ip', 'amount', 'product', 'value', 'payment_way', 'note', 'state',)
    list_display_links = ('buyer',)
    search_fields = ('buyer', 'cellphone', 'state',)
    list_filter = ('product', 'state',)
    fieldsets = (
        (None, {'fields': ('note', 'state',)}),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('order_number', 'buyer', 'cellphone', 'product', 'price', 'value', 'amount', 'email', 'address', 'payment_way', 'ip',),
        }),
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_number', 'firm', 'price', 'product_content', 'youtube',)
    list_display_links = ('name',)

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image',)
    list_display_links = ('product',)
    list_filter = ('product',)

@admin.register(SlideShow)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'page', 'image',)
    list_display_links = ('event_name',)
    list_filter = ('page',)

# Register your models here.
# admin.site.register(Product)
# admin.site.register(ProductImages)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(SlideShow)
