# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    DEGREE_CHOICES = (
        ("0", u"不可选"),
        ("1", u"可以选"),
    )
    # 学号
    u_number = models.IntegerField(verbose_name="学号", default=10011, max_length=20)
    # 昵称
    names = models.CharField(max_length=8, verbose_name=u"姓名", default="")
    # 班级
    classes = models.CharField(max_length=20, verbose_name=u"班级", default="")
    # 座位
    seat_status = models.CharField(choices=DEGREE_CHOICES, verbose_name="座位状态",  max_length=6, default='1')
    # 性别 只能男或女，默认女
    gender = models.CharField(max_length=7,verbose_name=u"性别",choices=GENDER_CHOICES,default="female")
    # 电话
    mobile = models.CharField(max_length=12, null=True, blank=True, verbose_name=u"电话")
    # word 文档链接
    pdf_url = models.CharField(max_length=50, null=True, blank=True, verbose_name="文档地址")
    # 学院
    college = models.CharField(max_length=10, verbose_name="学院", default="电信学院")
    # 校区
    campus = models.CharField(max_length=10, verbose_name="校区", default="官渡校区")
    # 特征码
    feature = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name="特征码")
    # 成绩
    grades = models.IntegerField(verbose_name="成绩", null=True, blank=True)

    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100,
        verbose_name=u"头像"
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
    def __str__(self):
        return self.username


class Week(models.Model):
    DATE_CHOICES = (
    ('1', u'星期一'), ('2', u'星期二'), ('3', u'星期三'), ('4', u'星期四'), ('5', u'星期五'), ('6', u'星期六'), ('7', u'星期天'),)
    dateTime = models.CharField(choices=DATE_CHOICES, verbose_name="星期", default=0, max_length=10)

    class Meta:
        verbose_name = "星期"
        verbose_name_plural = verbose_name
        ordering = ['-id']


    def __str__(self):
        return "星期{0}".format(self.dateTime)


class WTime(models.Model):
    CLASSES_CHOICES = (("12", u"1-2节课"), ("34", u"3-4节课"), ("56", u"5-6节课"), ("78", u'7-8节课'), ("90", u'9-10节课'),)
    classtime = models.CharField(choices=CLASSES_CHOICES, verbose_name="节课", default=0, max_length=10)
    week = models.ManyToManyField(Week, verbose_name="星期")

    class Meta:
        verbose_name = "节课"
        verbose_name_plural = verbose_name

    def get_dataTime(self):
        for b in self.week.all():
            b = b.dateTime
        return b

    def __str__(self):
        v = [b.dateTime for b in self.week.all()]
        return "星期{0} {1}节课".format(v, self.classtime)


class User_ex(models.Model):
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # 和User关联的外键
    email = models.CharField(max_length=24, verbose_name=u"邮箱", default="")
    valid_code = models.CharField(max_length=24)  # 验证码
    valid_time = models.DateTimeField(auto_now=True)  # 验证码有效时间
    starttime = models.DateField(auto_now_add=True, verbose_name="开始时间", blank=True, null=True)
    endtime = models.DateField(auto_now=True, verbose_name="结束时间", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.valid_code)


class Seat(models.Model):
    DEGREE_CHOICES = (("1", u"可以选"), ("0", u"不可选"), ("2", u"维修"),)
    DATE_CHOICES = (('1', u'星期一'), ('2', u'星期二'), ('3', u'星期三'), ('4', u'星期四'), ('5', u'星期五'), ('6', u'星期六'), ('7', u'星期天'),)
    CLASSES_CHOICES = (("12", u"1-2节课"), ("34", u"3-4节课"), ("56", u"5-6节课"), ("78", u'7-8节课'), ("90", u'9-10节课'),)

    # time = models.IntegerField(verbose_name="selectTime")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name="用户名")
    # dateTime = models.CharField(choices=DATE_CHOICES, verbose_name="星期", default=0, max_length=10)
    # classtime = models.CharField(choices=CLASSES_CHOICES, verbose_name="节课", default=0, max_length=10)
    status = models.CharField(choices=DEGREE_CHOICES, verbose_name="座位状态", default=1, max_length=10)
    starttime = models.DateField(auto_now_add=True, verbose_name="开始时间", blank=True, null=True)
    endtime = models.DateField(auto_now=True, verbose_name="结束时间", blank=True, null=True)
    number = models.IntegerField(verbose_name="座位号")
    week = models.ManyToManyField(WTime, verbose_name="节课")

    def get_dataTime(self):
        for week_id in self.week.all():
            week = week_id.classtime
            week1 = week_id.get_dataTime()
        return "{0}节".format(week)
    get_dataTime.short_description = "节课"

    def get_week(self):
        for week_id in self.week.all():
            week1 = week_id.get_dataTime()
        return "星期{0}".format(week1)
    get_week.short_description = "星期"

    class Meta:
        verbose_name = "座位状态"
        verbose_name_plural = verbose_name
        ordering = ['-number', ]

    def __str__(self):
        return str(self.number)


class Test(models.Model):

    class Meta:
        verbose_name = u"自定义页面"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Meta.verbose_name


# 轮播图model
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name=u"轮播图",
        max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    # 重载__str__方法使后台不再直接显示object
    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.title, self.index)


class EmailVerifyRecord(models.Model):
    # SEND_CHOICES = (
    #     ("register", u"注册"),
    #     ("forget", u"找回密码"),
    #     ("update_email", u"修改邮箱"),
    # )
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 未设置null = true blank = true 默认不可为空
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name=u"验证码类型")
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
