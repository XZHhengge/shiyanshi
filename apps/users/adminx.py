# _*_ coding: utf-8 _*_
__author__ = 'admin'
__date__ = '2018/9/27 13:55'
import xadmin
from django.contrib.auth.models import Group, Permission
from xadmin import views

from .models import Seat, Banner, WTime, Week, Test
# X admin的全局配置信息设置


class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "小新文：云计算实验室"
    site_footer = "24小时无人值守实验室"

    # 收起菜单
    # menu_style = "accordion"


class UserAdmin(object):
    list_display = ['u_number', 'names', 'gender', 'grades', 'get_seat', 'seat_status' ]
    search_fields = ['u_number', 'names', 'gender', 'grades', 'get_seat', 'seat_status']
    list_filter = ['u_number', 'names', 'gender', 'grades', 'seat_status']
    list_per_page = 50


class SeatAdmin(object):
    list_display = ['user', 'status', 'number', 'get_dataTime', 'get_week']
    search_fields = ['user', 'status', 'number', ]
    list_filter = ['user', 'status', 'number', ]
    relfield_style = 'fa-ajax'
    list_per_page = 50


class WeekAdmin(object):
    list_display = ['dateTime', ]
    search_fields = ['dateTime', ]
    list_filter = ['dateTime', ]
    list_per_page = 50


class WTimeAdmin(object):
    list_display = ['week', 'classtime', ]
    search_fields = ['week', 'classtime', ]
    list_filter =['week', 'classtime', ]
    list_per_page = 50


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time', ]
    search_fields = ['title', 'image', 'url', 'index', ]
    list_filter = ['title', 'image', 'url', 'index', 'add_time', ]
    list_per_page = 1


class TestAdmin(object):
    list_display = []
    object_list_template = 'hello.html'


# 将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserAdmin)
xadmin.site.register(Week, WeekAdmin)
xadmin.site.register(WTime, WTimeAdmin)
xadmin.site.register(Seat, SeatAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Test, TestAdmin)