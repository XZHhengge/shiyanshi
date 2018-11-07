# # -*- coding: utf-8 -*-
# from django import forms
# from django.core.exceptions import ValidationError
# from users.models import UserProfile
# from user_ex.models import User_ex
# from django.utils import timezone
#
#
# class ForgetPwdForm(forms.Form):
#     """Forget the password and try to find it"""
#     email = forms.EmailField(label=u'用户邮箱',
#                              # widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': u'请输入您注册时用的邮箱'})
#                              )
#     # pwd_1 = forms.CharField(label=u'新的密码', max_length=36,
#     #                         # widget=forms.PasswordInput(
#     #                             # attrs={'class': 'form-control', 'id': 'pwd_1', 'placeholder': u'请输入6-36位的密码'})
#     #                         )
#     # pwd_2 = forms.CharField(label=u'再输一遍', max_length=36,
#     #                         # widget=forms.PasswordInput(
#     #                             # attrs={'class': 'form-control', 'id': 'pwd_2', 'placeholder': u'重复新的密码确保正确'})
#     #                         )
#     check_code = forms.CharField(label=u'验证码',
#                                  # widget=forms.TextInput(
#                                  #     attrs={'class': 'form-control', 'id': 'check_code', 'placeholder': u'输入验证码'})
#                                  )
#
#     # 验证邮箱是否存在
#     # def clean_email(self):
#     #     email = self.cleaned_data.get('email')
#     #     users = UserProfile.objects.filter(email=email)
#     #
#     #     if users.count() == 0:
#     #         raise ValidationError(u'该邮箱没有被注册，请检查')
#     #     return email
#
#     # 验证两个新密码是否一致
#     # def clean_pwd_2(self):
#     #     pwd_1 = self.cleaned_data.get('pwd_1')
#     #     pwd_2 = self.cleaned_data.get('pwd_2')
#     #
#     #     if pwd_1 != pwd_2:
#     #         raise ValidationError(u'两次输入的密码不一致，再输入一次吧')
#     #     return pwd_2
#
#     # 验证验证码是否正确
#     # def clean_check_code(self):
#     #     try:
#     #         # 获取对应的用户
#     #         email = self.cleaned_data.get('email')
#     #         check_code = self.cleaned_data.get('check_code')
#     #         user = UserProfile.objects.get(email=email)
#     #
#     #         # 获取对应的用户拓展信息，验证验证码
#     #         user_ex = User_ex.objects.filter(user=user)
#     #         if user_ex.count > 0:
#     #             user_ex = user_ex[0]
#     #         else:
#     #             raise ValidationError(u'未获取验证码')
#     #
#     #         if user_ex.valid_code != check_code:
#     #             raise ValidationError(u'验证码不正确')
#     #
#     #         # 验证有效期
#     #         now = timezone.now()  # 用这个回去当前时间
#     #         create = user_ex.valid_time
#     #
#     #         # 两个datetime相减，得到datetime.timedelta类型
#     #         td = now - create
#     #         if td.seconds / 60 >= 10:
#     #             raise ValidationError(u'验证码失效')
#     #
#     #         return check_code
#     #     except Exception as e:
#     #         raise ValidationError(u'验证码不正确或失效')