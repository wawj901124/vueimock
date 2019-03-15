from datetime import datetime   #导入系统时间包
from django.db import models    #导入django model包
from django.contrib.auth import  get_user_model  #导入get_user_model

from goods.models import Goods

User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值
# Create your models here.
class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.PROTECT)
    goods = models.ForeignKey(Goods, verbose_name=u"商品", on_delete=models.PROTECT)
    nums = models.IntegerField(default=0, verbose_name="购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)
