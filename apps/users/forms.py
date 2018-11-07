# _*_ coding: utf-8 _*_
__author__ = 'admin'
__date__ = '2018/9/27 20:57'

from django import forms
from django.core.exceptions import ValidationError    # 登录表单验证
from .models import UserProfile, User_ex
from django.utils import timezone
# from captcha.fields import CaptchaField
# from django.contrib.auth.models import User


class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)


# 用于个人中心修改个人信息
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['names', 'u_number', 'gender', 'mobile', 'classes', 'college', 'campus', 'email', ]

# 个人中心上传图片
class UploadImageForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['image', ]


# 重置密码form实现
class ModifyPwdForm(forms.Form):
    # 密码不能小于5位
    password1 = forms.CharField(required=True, min_length=5)
    # 密码不能小于5位
    password2 = forms.CharField(required=True, min_length=5)


# 验证码form & 注册表单form
class RegisterForm(forms.Form):
    # 此处email与前端name需保持一致。
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)
    # 验证码
    # # 应用验证码 自定义错误输出key必须与异常一样
# 座位Form
class SeatForm(forms.Form):
    date = forms.CharField()
    time = forms.CharField()
    label = forms.CharField()

# class Code():
#     email = forms.CharField()


class RegForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    email = forms.EmailField(required=True)
    verification_code = forms.CharField(required=True)

    #
    # username = forms.CharField(
    #     # label='用户名',
    #     max_length=30,
    #     min_length=3,
    #     # widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入3-30位用户名'})
    # )
    # email = forms.EmailField(
    #     label='邮箱',
    #     # widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'请输入邮箱'})
    # )
    # verification_code = forms.CharField(
    #     label='验证码',
    #     # widget=forms.TextInput(
    #     #     attrs={'class':'form-control', 'placeholder':'点击“发送验证码”发送到邮箱'}
    #     # )
    # )
    # password = forms.CharField(
    #     label='密码',
    #     min_length=6,
    #     # widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请输入密码'})
    # )

    # def __init__(self, *args, **kwargs):
    #     if 'request' in kwargs:
    #         self.request = kwargs.pop('request')
    #     super(RegForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     # try:
    #         # 获取对应的用户
    #         email = self.cleaned_data.get('email')
    #         verification_code = self.cleaned_data.get('verification_code', '')
    #         # check_code = self.cleaned_data.get('check_code')
    #         # user = UserProfile.objects.get(email=email)
    #
    #         # 获取对应的用户拓展信息，验证验证码
    #         user_ex = User_ex.objects.get(valid_code=verification_code)
    #         # if user_ex.count > 0:
    #         #     user_ex = user_ex[0]
    #         # else:
    #         #     raise ValidationError(u'未获取验证码')
    #         print('前端页面：'+ verification_code)
    #         if user_ex.email != email:
    #             print(user_ex.valid_code)
    #             raise ValidationError(u'验证码不正确')
    #         print('密码验证成功')
    #
    #         # 验证有效期
    #         now = timezone.now()  # 用这个回去当前时间
    #         create = user_ex.valid_time
    #
    #         # 两个datetime相减，得到datetime.timedelta类型
    #         td = now - create
    #         if td.seconds / 60 >= 10:
    #             raise ValidationError(u'验证码失效')
    #
    #         return verification_code
        # except Exception as e:
        #     raise ValidationError(u'验证码不正确或失效')

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if UserProfile.objects.filter(email=email).exists():
    #         raise forms.ValidationError('邮箱已存在')
    #     return email

    # def clean_password_again(self):
    #     password = self.cleaned_data['password']
    #     password_again = self.cleaned_data['password_again']
    #     if password != password_again:
    #         raise forms.ValidationError('两次输入的密码不一致')
    #     return password_again

    # def clean_verification_code(self):
    #     verification_code = self.cleaned_data.get('verification_code', '').strip()
    #     print(verification_code)
    #     if verification_code == '':
    #         raise forms.ValidationError('验证码不能为空')
    #     return verification_code


# 忘记密码
# class ForgetForm(forms.Form):
#     email = forms.EmailField(required=True)
    # captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgotPasswordForm(forms.Form):

    email = forms.EmailField(required=True)
    verification_code = forms.CharField(required=True)
    new_password = forms.CharField(required=True, min_length=5)

    # email = forms.EmailField(
    #     label='邮箱',
    #     widget=forms.EmailInput(
    #         attrs={'class':'form-control', 'placeholder':'请输入绑定过的邮箱'}
    #     )
    # )
    # verification_code = forms.CharField(
    #     label='验证码',
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={'class':'form-control', 'placeholder': '点击“发送验证码”发送到邮箱'}
    #     )
    # )
    # new_password = forms.CharField(
    #     label='新的密码',
    #     widget=forms.PasswordInput(
    #         attrs={'class':'form-control', 'placeholder': '请输入新的密码'}
    #     )
    # )

    # def __init__(self, *args, **kwargs):
    #     if 'request' in kwargs:
    #         self.request = kwargs.pop('request')
    #     super(ForgotPasswordForm, self).__init__(*args, **kwargs)

    # def clean_email(self):
    #     email = self.cleaned_data['email'].strip()
    #     if not UserProfile.objects.filter(email=email).exists():
    #         raise forms.ValidationError('邮箱不存在')
    #     return email

    # def clean_verification_code(self):
    #     email = self.cleaned_data.get('email')
    #     verification_code = self.cleaned_data.get('verification_code', '').strip()
    #     if verification_code == '':
    #         print('验证码不能为空')
    #         raise forms.ValidationError('验证码不能为空')
    #
    #     # 判断验证码
    #     user_ex = User_ex.objects.get(email=email)
    #     code = user_ex.valid_code
    #     verification_code = self.cleaned_data.get('verification_code', '')
    #     if not (code != '' and code == verification_code):
    #         print(code)
    #         print(verification_code)
    #         print('验证码不正确')
    #         raise forms.ValidationError('验证码不正确')
    #
    #     return verification_code