#  -*- encoding:utf8 -*-
from __future__ import unicode_literals
from datetime import datetime
# 自带package

from django.contrib.auth.models import AbstractUser
from django.db import models


# 第三方package


# 自定义
# Create your models here.

# 覆盖默认user,AbstractUser作为基类


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=10, verbose_name=u"昵称", default="")
    birthday = models.DateField(null=True, blank=True, verbose_name=u"生日")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u'image/default.png')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVertifyRecoder(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(('register', u"注册"), ("forget", u"忘记密码")), max_length=10,
                                 verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.email


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.email
