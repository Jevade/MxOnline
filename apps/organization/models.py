# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from courses.models import Course


# Create your models here.


class CityDict(models.Model):
    """
    所在城市
    """
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.CharField(max_length=300, verbose_name=u"机构描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    """
    课程机构
    """
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    """

    课程机构  
    """

    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    work_years = models.IntegerField(default=0, verbose_name=u"教学年限")
    work_company = models.CharField(max_length=50, verbose_name=u"单位")
    work_position = models.CharField(max_length=50, verbose_name=u"职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"讲师"
        verbose_name_plural = verbose_name
