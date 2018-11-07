# # -*- coding: utf-8 -*-
# # from django.http import HttpResponse
# # from django.shortcuts import render_to_response, render
# # from django.contrib.auth import logout, authenticate, login
# # from users.models import UserProfile
# # from django.core.mail import EmailMultiAlternatives
# # import json, time, datetime, random, string
# #
# # from user_ex.form import ForgetPwdForm
# # from user_ex.models import User_ex
# # from django.utils import timezone
# #
#
# # def password_lost(request):
# #     """forgot password deals"""
# #     data = {}
# #     data['form_title'] = u'重置密码'
# #     data['submit_name'] = u'　确定　'
# #
# #     if request.method == 'POST':
# #         # 表单提交
# #         form = ForgetPwdForm(request.POST)
# #
# #         # 验证是否合法
# #         if form.is_valid():
# #             # 修改数据库
# #             email = form.cleaned_data['email']
# #             pwd = form.cleaned_data['pwd_2']
# #             user = User.objects.get(email=email)
# #             user.set_password(pwd)
# #             user.save()
# #
# #             # 删除验证码
# #             ex = User_ex.objects.filter(user=user)
# #             if ex.count() > 0:
# #                 ex.delete()
# #
# #             # 重新登录
# #             user = authenticate(username=user.username, password=pwd)
# #             if user is not None:
# #                 login(request, user)
# #
# #             # 页面提示
# #             data['goto_url'] = reverse('user_info')
# #             data['goto_time'] = 3000
# #             data['goto_page'] = True
# #             data['message'] = u'重置密码成功，请牢记新密码'
# #             return render_to_response('message.html', data)
# #     else:
# #         # 正常加载
# #         form = ForgetPwdForm()
# #     data['form'] = form
# #     return render(request, 'user/pwd_forget.html', data)
#
#
# def get_email_code(request):
#     """get email code"""
#     email = request.GET.get('email', '')
#     code = ''.join(random.sample(string.digits + string.ascii_letters, 6))
#
#     data = {}
#     data['success'] = False
#     data['message'] = ''
#
#     try:
#         # 检查邮箱
#         users = UserProfile.objects.filter(email=email)
#         if len(users) == 0:
#             data['success'] = False
#             data['message'] = u'此邮箱未注册'
#             raise Exception (data['message'])
#             # raise Exception, data['message']
#
#         user = users[0]
#
#         # 检查短时间内是否有生成过验证码
#         user_ex = User_ex.objects.filter(user=user)
#         if len(user_ex) > 0:
#             user_ex = user_ex[0]
#
#             # 两个datetime相减，得到datetime.timedelta类型
#             create_time = user_ex.valid_time
#             td = timezone.now() - create_time
#             if td.seconds < 60:
#                 data['message'] = u'1分钟内发送过一次验证码'
#                 raise Exception(data['message'])
#         else:
#             # 没有则新建
#             user_ex = User_ex(user=user)
#
#         # 写入数据库
#         user_ex.valid_code = code
#         print(code)
#         user_ex.valid_time = timezone.now()
#         user_ex.save()
#
#         # 发送邮件
#         subject = u'[13035822385@163.com]激活您的帐号'
#         message = u"""
#             <h2>广油 24小时无人值守实验室<h2><br />
#             <p>验证码(有效期10分钟)：%s</p>
#             <p><br/>(请保管好您的验证码)</p>
#             """ % code
#
#         send_to = [email]
#         fail_silently = True  # 发送异常不报错
#
#         msg = EmailMultiAlternatives(subject=subject, body=message, to=send_to)
#         msg.attach_alternative(message, "text/html")
#         msg.send(fail_silently)
#
#         data['success'] = True
#         data['message'] = 'OK'
#     except Exception as e:
#         pass
#     finally:
#         return HttpResponse(json.dumps(data), content_type="application/json")