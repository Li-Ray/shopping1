from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<number>\w{3,8})$', views.product_detail, name='product_detail'),
    url(r'^(?P<number>\w{3,8})/add', views.add_order, name='add_order'),
    url(r'^new_product', views.new_product, name='new_product'),
    url(r'^all_product', views.all_product, name='all_product'),
    url(r'', views.index, name='index'),
]