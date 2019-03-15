import xadmin   #  导入xadmin

from django.contrib.auth import  get_user_model  #导入get_user_model
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值


class UserAdmin(object):
    list_display = ["id","name"]
    search_fields = ["name"]
    list_editable = ["name"]  # 可以在列表页对字段进行编辑
    list_filter = ["name"]
    model_icon = 'fa fa-eye'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time']  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    list_display_links = ["name", ]  # 设置点击链接进入编辑页面的字段
    show_detail_fields = ["name", ]  # 显示数据详情


# xadmin.site.register(User,UserAdmin)  #在xadmin中注册UserAdmin