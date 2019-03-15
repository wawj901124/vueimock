import django_filters   #导入django_filters
from django.db.models import Q   #导入Q   ，可使用或，与运算符
# from rest_framework.filters

from .models import ShoppingCart


class ShoppingCartFilter(django_filters.rest_framework.FilterSet):#继承django_filters.rest_framework.FilterSet
    """
    购物车的过滤类
    """
    # pricemin = django_filters.NumberFilter(name="shop_price",help_text="最低价格" , lookup_expr='gte')   #name规定检索的字段，lookup_expr规定操作的类型,gte表示大于等于
    # pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte') #lte表示小于等于
    # name = django_filters.CharFilter(name='name',lookup_expr='icontains')  #lookup_expr='icontains'表示操作的类型为“contains”，前面的i表示忽略大小写
                                                                            #配置name为模糊搜索 #不指定lookup_expr，就是全部匹配
    # name = django_filters.CharFilter(name='name')  #不指定lookup_expr，就是全部匹配
    # top_category = django_filters.NumberFilter(method='top_category_filter')    #外键的过滤要用NumberFilter，外键实际是个Number
                                                            #method,可以自己传递一个函数进来,可以自定义过滤的函数

    #自定义查找第一类别的所有商品
    # def top_category_filter(self,queryset,name,value): #queryset,name,value这三个参数会默认传递进来，需要将参数写进来
    #     queryset = queryset.filter(Q(category_id = value)| Q(category__parent_category_id = value)| Q(category__parent_category__parent_category_id = value))
    #                     #category_id等于传进来的value 或者 category的父的category_id等于传进来的value或者category的父的category的父的category_id等于传进来的value
    #     return queryset   #返回queryset
    # priceLevel = django_filters.CharFilter(method='priceLevel_filter',help_text="商品价格级别",)   #自定义价格过滤

    #自定义价格过滤  过滤学习网址：https://www.cnblogs.com/yoyo008/p/9076200.html；
    # https://blog.csdn.net/vic_torsun/article/details/69791170；
    # https://blog.csdn.net/weixin_40907382/article/details/79242989
    # def priceLevel_filter(self,queryset,name,value):#queryset,name,value这三个参数会默认传递进来，需要将参数写进来
    #     if value=='0':
    #         # queryset = queryset.filter(Q(shop_price__gte=0)& Q(shop_price__lt =500))
    #         queryset = queryset.filter(shop_price__range=(0,500))
    #     elif value =='1':
    #         queryset = queryset.filter(shop_price__range=(500,1000))
    #     elif value == '2':
    #         queryset = queryset.filter(shop_price__range=(1000, 2000))
    #     elif value == '5':
    #         queryset = queryset.filter(shop_price__range=(2000, 5000))
    #     return queryset   #返回queryset




    class Meta:
        model = ShoppingCart   #指定模型
        fields = ['goods']
        # fields = ['pricemin', 'pricemax','name']   #指定字段
                                #添加“is_hot”字段来过滤是否热销商品
