import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'shiyanshi.settings'
from django.core.mail import send_mail
from django.conf import settings
settings.configured()
send_mail(

    '绑定邮箱',
'验证码：%s' % 124514,
'1075605131@qq.com',
['13035822385@163.com'],
fail_silently = False,)