from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'',views.index, name='index'),
    url(r'^(?P<number>\w{3,8})$', views.product_detail, name='product_detail'),
    url(r'^(?P<number>\w{3,8})/add', views.add_order, name='add_order'),
]