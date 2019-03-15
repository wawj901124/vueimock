from django.shortcuts import render

from rest_framework.response import Response #导入Response，drf的Response，远比django中的Response强大
from rest_framework.pagination import PageNumberPagination   #导入PageNumberPagination
from rest_framework import viewsets   #viewsets，一个很重要的view
from rest_framework import  filters   #搜索过滤用
from django_filters.rest_framework import DjangoFilterBackend   #导入 DjangoFilterBackend，字段过滤用
from rest_framework_extensions.cache.mixins import CacheResponseMixin   #导入缓存机制包CacheResponseMixin
from rest_framework import mixins   #导入mixins
from rest_framework import generics   #导入generics

from .models import ShoppingCart   #  导入ShoppingCart
from .serializers import ShoppingCartSerializer  #  导入ShoppingCart Serializer
from .filters import ShoppingCartFilter  #  导入ShoppingCart Filter

from django.views.decorators.csrf import csrf_exempt   #屏蔽CSRF



# Create your views here.

class ShoppingCartPagination(PageNumberPagination):   #定制化rest framework 的分页的配置,继承PageNumberPagination
    page_size = 2  #默认显示12条
    page_size_query_param = 'page_size'   #指明向后台要多少条，指定这页有多少个
    page_query_param = 'page'   #指明访问页的参数，代表请求多少页
    max_page_size = 100   #最大的页面最大的数量只能是100个，最大可显示100条

# @csrf_exempt  #屏蔽CSRF
class ShoppingCartViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    """
    商品列表页,分页，搜索，过滤，排序
    """
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer  # serializer类
    pagination_class = ShoppingCartPagination   #设置分页的类为定制的GoodsPagination的类 ，
                                        # 可以代替在Settings中对REST_FRAMEWORK 的配置
    #字段过滤
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)   #配置过滤：配置精准过滤，过滤的内容要完全等于输入的内容
                        #DjangoFilterBackend字段过滤，filters.SearchFilter为搜索过滤,filters.OrderingFilter为排序过滤
    filter_class = ShoppingCartFilter  # 配置过滤，配置过滤类
    search_fields = ('goods',)  #配置搜索过滤,name,表示在这个name字段内容里,进行模糊搜索
    # search_fields = ('^name','goods_brief','goods_desc')   #配置搜索过滤,^name,表示在这个name字段内容里，搜索以输入内容开头的内容
    # search_fields = ('=name', 'goods_brief', 'goods_desc')  # 配置搜索过滤,=name,表示在这个字段内容里，搜索完全等于输入内容的内容
    ordering_fields = ('nums',)   #配置排序过滤:销量和价格
