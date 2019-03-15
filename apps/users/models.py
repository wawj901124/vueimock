from datetime import datetime   #系统的包放在最上面

from django.db import models   #第二个级别的就是第三方包
from django.contrib.auth.models import AbstractUser   #导入django的用户模块

#第三个就是我们自己创建的包
# Create your models here.


class UserProfile(AbstractUser):#继承django的user模块，其中包含的字段都有，以下是新增的字段
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")  #null=True.表示实例化的时候可以为空，blank=True表示填写的内容可以为空
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female", null=True, blank=True, verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural =verbose_name

    def __str__(self):#重载函数
        return self.username