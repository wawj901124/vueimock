"""vueimock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

import xadmin   #导入xadmin
from vueimock.settings import MEDIA_ROOT   #访问图片配置，导入MEDIA_ROOT
from django.views.static import serve  #访问图片配置，导入django.views.static（专门做静态文件的）中的serve
from rest_framework.documentation import include_docs_urls   #导入include_docs_urls,可以查看文档
from rest_framework.routers import DefaultRouter   #导入DefaultRouter，使用routers，让url配置更简单
from rest_framework.authtoken import views   #配置token路径 2-1,导入authtoken的views

from goods.views import GoodsViewSet  #  导入GoodsViewSet
from trade.views import ShoppingCartViewSet   #  导入ShoppingCartViewSet
from users.views import UserViewSet  #  导入UserViewSet


router = DefaultRouter()   #实例化
#配置goods的url
router.register('goods', GoodsViewSet,base_name='goods')  #将goods注册到router中，后期大部分的url都会基于这个来配置
            #router已经自动绑定post请求到create方法中，自动绑定get请求到list方法中

#配置ShoppingCart的url
router.register('shopcarts', ShoppingCartViewSet,base_name='shopcarts')  #将shopcarts注册到router中，后期大部分的url都会基于这个来配置
            #router已经自动绑定post请求到create方法中，自动绑定get请求到list方法中

#配置User的url
router.register('users', UserViewSet,base_name='users')  #将users注册到router中，后期大部分的url都会基于这个来配置
            #router已经自动绑定post请求到create方法中，自动绑定get请求到list方法中

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('media/<path:path>',serve,{"document_root":MEDIA_ROOT}), #访问图片配置，url配置
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework')), #drf登录的配置
    path('docs/', include_docs_urls(title="慕学生鲜")),  # include_docs_urls路径配置
    path( '',include(router.urls)),   #配置router路径

    # 获取token的url   #drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),  # 配置token路径，2-2，配置url

]
