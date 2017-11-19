from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, ProductImages, SlideShow , Order
import time, secrets
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):

    products = Product.objects.all()
    paginator = Paginator(products, 20)  # Show 20 contacts per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
        # If page is not an integer, deliver first page.
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        # If page is out of range, deliver last page of results.

    images = {}
    for i in products:
        image = ProductImages.objects.filter(product_id=i.id).first()
        images[image.product_id] = str(image.image)

    FirstSlide = SlideShow.objects.filter(page='1').last()
    SecondSlide = SlideShow.objects.filter(page='2').last()
    ThirdSlide = SlideShow.objects.filter(page='3').last()

    return render(request, 'index.html', {'products': products, 'images': images, 'FirstSlide': FirstSlide, 'SecondSlide': SecondSlide, 'ThirdSlide': ThirdSlide, 'paginator': paginator})

@csrf_protect
def add_order(request, number):
    # try:
        product = Product.objects.get(product_number=number)
        if request.method=="POST":
            time_now = time.strftime("%Y%m%d%H%M%S")
            rand_hex = secrets.token_hex(8)
            name = request.POST.get('name')
            cellphone=request.POST.get('cellphone')
            email=request.POST.get('email')
            address=request.POST.get('address')
            payment_way=request.POST.get('payment_way')
            note=request.POST.get('note')
            value=request.POST.get('values')
            order = Order.objects.create(
                order_number=time_now+rand_hex,
                buyer=name,
                cellphone=cellphone,
                product_id=product.id,
                price=product.price,
                value=value,
                amount=int(product.price)*int(value),
                address=address,
                email=email,
                payment_way=payment_way,
                ip=request.META['REMOTE_ADDR'],
                note=note,
            )
            return render(request, 'order_success.html')
    # except:
    #     return HttpResponse("訂購失敗，請重新訂購")


def product_detail(request, number):
    products = Product.objects.filter(product_number=number)
    images = ProductImages.objects.filter(product__product_number=number)
    return render(request, 'product.html', {'products': products, 'images': images, 'number':number })