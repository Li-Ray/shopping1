from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from products.models import Product, ProductImages, Order, SlideShow
from django.template import Context

# Create your views here.
def index(request):
    products = Product.objects.all()
    images = {}
    for i in products:
            image = ProductImages.objects.filter(product_id=i.id).first()
            images[image.product_id] = str(image.image)
    FirstSlide = SlideShow.objects.filter(page='1').last()
    SecondSlide = SlideShow.objects.filter(page='2').last()
    ThirdSlide = SlideShow.objects.filter(page='3').last()

    return render_to_response('index.html', {'products': products, 'images': images, 'FirstSlide': FirstSlide, 'SecondSlide': SecondSlide, 'ThirdSlide': ThirdSlide })

def add_order(request, number):
    #order = Order.objects.create()
    return HttpResponse("添加{}".format(number))

def product_detail(request, number):
    product = Product.objects.filter(product_number=number)
    images = ProductImages.objects.filter(product__product_number=number)
    return render_to_response('product.html', {'product': product, 'images': images })