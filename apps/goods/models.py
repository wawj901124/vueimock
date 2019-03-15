from datetime import datetime   #导入系统时间包
from django.db import models    #导入django model包


# Create your models here.
class Goods(models.Model):
    """
    商品
    """
    name = models.CharField(max_length=100, verbose_name="商品名")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name