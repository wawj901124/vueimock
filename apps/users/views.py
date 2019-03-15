from django.shortcuts import render

from rest_framework.response import Response #导入Response，drf的Response，远比django中的Response强大
from rest_framework.pagination import PageNumberPagination   #导入PageNumberPagination
from rest_framework import viewsets   #viewsets，一个很重要的view
from rest_framework import  filters   #搜索过滤用
from django_filters.rest_framework import DjangoFilterBackend   #导入 DjangoFilterBackend，字段过滤用
from rest_framework_extensions.cache.mixins import CacheResponseMixin   #导入缓存机制包CacheResponseMixin
from rest_framework import mixins   #导入mixins
from rest_framework import generics   #导入generics
from django.contrib.auth import  get_user_model  #导入get_user_model
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值
from django.contrib.auth.backends import ModelBackend   #导入ModelBackend
from django.db.models import Q   #导入Q，使用或、与用


from .serializers import UserSerializer  #  导入UserSerializer
from .filters import UserFilter  #  导入UserFilter

from django.views.decorators.csrf import csrf_exempt   #屏蔽CSRF



# Create your views here.

class UserPagination(PageNumberPagination):   #定制化rest framework 的分页的配置,继承PageNumberPagination
    page_size = 2  #默认显示12条
    page_size_query_param = 'page_size'   #指明向后台要多少条，指定这页有多少个
    page_query_param = 'page'   #指明访问页的参数，代表请求多少页
    max_page_size = 100   #最大的页面最大的数量只能是100个，最大可显示100条

# @csrf_exempt  #屏蔽CSRF
class UserViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    """
    商品列表页,分页，搜索，过滤，排序
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer  # serializer类
    pagination_class = UserPagination   #设置分页的类为定制的GoodsPagination的类 ，
                                        # 可以代替在Settings中对REST_FRAMEWORK 的配置
    #字段过滤
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)   #配置过滤：配置精准过滤，过滤的内容要完全等于输入的内容
                        #DjangoFilterBackend字段过滤，filters.SearchFilter为搜索过滤,filters.OrderingFilter为排序过滤
    filter_class = UserFilter  # 配置过滤，配置过滤类
    search_fields = ('name',)  #配置搜索过滤,name,表示在这个name字段内容里,进行模糊搜索
    # search_fields = ('^name','goods_brief','goods_desc')   #配置搜索过滤,^name,表示在这个name字段内容里，搜索以输入内容开头的内容
    # search_fields = ('=name', 'goods_brief', 'goods_desc')  # 配置搜索过滤,=name,表示在这个字段内容里，搜索完全等于输入内容的内容
    ordering_fields = ('name',)   #配置排序过滤:销量和价格



# #自定义用户登录函数，一定要继承ModelBackend，然后重写里面的authenticate函数
# class CustomBackend(ModelBackend):
#     """
#     自定义用户验证
#     """
#     def authenticate(self,username=None,password=None, **kwargs):
#         try:
#             user = User.objects.get(Q(username=username)|Q( mobile=username))
#             if user.check_password(password):   #传递的明文密码，调用check_password，就会对password进行加密然后比较
#                 return user
#         except Exception as e:
#             return None