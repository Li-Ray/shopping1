from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from products.models import Product, ProductImages, Order

# Create your views here.
def index(request):
    product = Product.objects.all()
    #images = ProductImages.objects.all().filter(product_id=product.)
    return render(request, 'index.html', {'product': product})

def add_order(request, number):
    order = Order.objects.create()
    return HttpResponse("添加{}".format(number))

def product_detail(request, number):
    product = Product.objects.filter(product_number=number)
    images = ProductImages.objects.all()
    return render(request, 'product.html', {'product': product, 'images': images })
        #HttpResponse("產品{}的詳細資料".format(number))