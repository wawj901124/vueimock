from django.shortcuts import render

from rest_framework.response import Response #导入Response，drf的Response，远比django中的Response强大
from rest_framework.pagination import PageNumberPagination   #导入PageNumberPagination
from rest_framework import viewsets   #viewsets，一个很重要的view
from rest_framework import  filters   #搜索过滤用
from django_filters.rest_framework import DjangoFilterBackend   #导入 DjangoFilterBackend，字段过滤用
from rest_framework_extensions.cache.mixins import CacheResponseMixin   #导入缓存机制包CacheResponseMixin
from rest_framework import mixins   #导入mixins
from rest_framework import generics   #导入generics

from .models import Goods   #  导入Goods
from .serializers import GoodsSerializer  #  导入GoodsSerializer
from .filters import GoodsFilter  #  导入GoodsFilter


# Create your views here.
class GoodsPagination(PageNumberPagination):   #定制化rest framework 的分页的配置,继承PageNumberPagination
    page_size = 2  #默认显示12条
    page_size_query_param = 'page_size'   #指明向后台要多少条，指定这页有多少个
    page_query_param = 'page'   #指明访问页的参数，代表请求多少页
    max_page_size = 100   #最大的页面最大的数量只能是100个，最大可显示100条


class GoodsViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    """
    商品列表页,分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer  # serializer类
    pagination_class = GoodsPagination   #设置分页的类为定制的GoodsPagination的类 ，
                                        # 可以代替在Settings中对REST_FRAMEWORK 的配置
    #字段过滤
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)   #配置过滤：配置精准过滤，过滤的内容要完全等于输入的内容
                        #DjangoFilterBackend字段过滤，filters.SearchFilter为搜索过滤,filters.OrderingFilter为排序过滤
    filter_class = GoodsFilter  # 配置过滤，配置过滤类
    search_fields = ('name',)  #配置搜索过滤,name,表示在这个name字段内容里,进行模糊搜索
    # search_fields = ('^name','goods_brief','goods_desc')   #配置搜索过滤,^name,表示在这个name字段内容里，搜索以输入内容开头的内容
    # search_fields = ('=name', 'goods_brief', 'goods_desc')  # 配置搜索过滤,=name,表示在这个字段内容里，搜索完全等于输入内容的内容
    ordering_fields = ('shop_price',)   #配置排序过滤:销量和价格


