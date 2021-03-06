from django.db import models

# Create your models here.

class Product(models.Model):
    product_number=models.CharField("產品編號", max_length=30)
    name = models.CharField("產品名", max_length=30)
    firm = models.CharField("公司", max_length=30)
    price = models.PositiveIntegerField("價格")
    product_content = models.TextField("內容")
    youtube = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '產品'
        verbose_name_plural = verbose_name

class ProductImages(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = '產品圖'
        verbose_name_plural = verbose_name

class Order(models.Model):
    order_number=models.CharField(max_length=30)
    buyer = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=20)
    product = models.ForeignKey(Product)
    price = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    ip = models.CharField(max_length=30)
    note = models.TextField(null=True, blank=True  )
    buyed_time = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=30)
    shiped_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.buyer

    class Meta:
        verbose_name = '訂單'
        verbose_name_plural = verbose_name