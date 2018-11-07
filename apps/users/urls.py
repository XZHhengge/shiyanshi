# _*_ coding: utf-8 _*_
__author__ = 'admin'
__date__ = '2018/9/27 20:59'
from django.conf.urls import url
from django.urls import path
from .views import LoginForm, UserInfoView, SomeView, Seats, ChoiceTime
from .views import UploadImageView, UpdatePwdView, BespeakView,Word, UpdateEmailView, SendEmailCodeView
from . import views

app_name = "users"
urlpatterns = [
    # 用户信息
    path('info/', UserInfoView.as_view(), name="user_info"),
    path('pdf/', SomeView.as_view(), name="user_pdf"),
    path('upload/', UploadImageView.as_view(), name="image_upload"),
    path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    path('bespeak', BespeakView.as_view(), name="user_bespeak"),
    path('word/',Word.as_view(),name="word"),
    path('getSeat/', Seats.as_view(), name='getSeat'),
    path(r'choice/', ChoiceTime.as_view(), name= 'choicetime'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('forgetpassword/', views.forgetpassword, name='fogetpassword'),
    path('update_email/', UpdateEmailView.as_view(), name="update_email"),
    path('sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),
    #注册链接
    # path('')

]