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
    product = models.ForeignKey(Product, verbose_name="產品名")
    image = models.ImageField(upload_to='static/images', verbose_name="產品圖")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = '產品圖'
        verbose_name_plural = verbose_name

class Order(models.Model):
    order_number=models.CharField(max_length=50, verbose_name="訂單號碼")
    buyer = models.CharField(max_length=30, verbose_name="訂購人")
    cellphone = models.CharField(max_length=20, verbose_name="電話")
    product = models.ForeignKey(Product, verbose_name="產品")
    price = models.PositiveIntegerField(verbose_name="單價")
    value = models.PositiveIntegerField(verbose_name="數量")
    amount = models.PositiveIntegerField(verbose_name="總價")
    email= models.EmailField()
    address = models.CharField(max_length=200, verbose_name="地址")
    payment_way = models.CharField(max_length=30, verbose_name="付款方式")
    ip = models.CharField(max_length=30)
    note = models.TextField(blank=True, verbose_name="備註")
    buyed_time = models.DateTimeField(auto_now_add=True, verbose_name="訂購時間")
    StateChoices = (('未處理', '未處理'), ('已出貨', '已出貨'), ('待確認', '待確認'), ('註銷', '註銷'))
    state = models.CharField(max_length=30,choices=StateChoices,default='未處理', verbose_name="狀態")
    shipped_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.buyer

    class Meta:
        verbose_name = '訂單'
        verbose_name_plural = verbose_name

class SlideShow(models.Model):
    event_name = models.CharField(max_length=30)
    PageChoices = (('1', 'First Slide'),('2', 'Second Slide'),('3', 'Third Slide'))
    page = models.CharField(max_length=1,choices=PageChoices,default=1)
    image = models.ImageField(upload_to='static/images/slideshow')

    def __str__(self):
        return self.event_name