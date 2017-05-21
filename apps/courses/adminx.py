# -*- coding:utf-8 -*-
__author__ = 'Jevade'
__data__ = '2017/5/20 10:27'

from datetime import datetime

import xadmin
from django.db import models

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'degree', 'desc', 'detail', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'degree', 'desc', 'detail', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'degree', 'desc', 'detail', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['lesson', 'name', 'download', 'add_time']
    search_fields = ['lesson', 'name', 'download']
    list_filter = ['lesson', 'name', 'download', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
