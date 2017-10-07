from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from products.models import Product, ProductImages, Order
from django.template import Context

# Create your views here.
def index(request):
    products = Product.objects.all()
    images = {}

    for i in products:
            image = ProductImages.objects.filter(product_id=i.id).first()
            images[image.product_id] = str(image.image)

    return render_to_response('index.html', {'products': products, 'images': images})

def add_order(request, number):
    #order = Order.objects.create()
    return HttpResponse("添加{}".format(number))

def product_detail(request, number):
    product = Product.objects.filter(product_number=number)
    images = ProductImages.objects.all()
    return render_to_response('product.html', {'product': product, 'images': images })
        #HttpResponse("產品{}的詳細資料".format(number))