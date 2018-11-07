"""shiyanshi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url
# 导入x admin，替换admin
from django.views.static import serve
from .settings import MEDIA_ROOT
    # STATIC_ROOT
import extra_apps.xadmin as xadmin
from apps.users.views import LoginView, IndexView, LogoutView, RegisterView,ForgetPwdView
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # path('admin/', admin.site.urls),

    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # 登录
    path('', LoginView.as_view(), name="login"),
    # 主页
    path('index/', IndexView.as_view(), name="index"),
    # 退出
    path('logout/', LogoutView.as_view(), name="logout"),

    path('users/', include('users.urls', namespace='users')),
    # 文档管理器
    path('xadmin/doc/', include('django.contrib.admindocs.urls')),
    # # 验证码
    # path('captcha/', include('captcha.urls')),

    path('admin/doc/', include('django.contrib.admindocs.urls')),

    path('register/', RegisterView.as_view(), name="register"),

    # re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),

    # path(r'^static/(?P<path>.*)$', serve,
    #     {'document_root': STATIC_ROOT},name='static'),
    # path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    # # 注册url
    # path("register/", RegisterView.as_view(), name="register"),
    # # 修改密码
    # path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),
    # 激活用户url
    # re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),

]
#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'