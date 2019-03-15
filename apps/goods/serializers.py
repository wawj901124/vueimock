from rest_framework import serializers   #导入serializers


from .models import Goods



#商品序列化
class GoodsSerializer(serializers.ModelSerializer):   #  继承serializers.ModelSerializer
    add_time = serializers.DateTimeField(read_only=True,format="%Y-%m-%d %H:%M:%S")   #read_only=True,表示这个字段只返回不提交
                            #format="%Y-%m-%d %H:%M"，表示格式化时间显示   #设置添加时间字段为只能读，不能写
    class Meta:
        model = Goods   #  指明model
        fields = "__all__"#取出model中的所有字段，不管是什么字段都不会序列化出错，而且会将外键序列化成他的ID
                                #图片类型的路径加上media配置的路径
                                #时间类型也不会出错


