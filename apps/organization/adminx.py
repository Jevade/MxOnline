# -*- coding:utf-8 -*-
__author__ = 'Jevade'
__data__ = '2017/5/20 10:27'

from datetime import datetime

import xadmin
from django.db import models

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'detail', 'students', 'fav_nums', 'image', 'click_nums', 'address', 'city',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'students', 'fav_nums', 'image', 'click_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'detail', 'students', 'fav_nums', 'image', 'click_nums', 'address', 'city',
                   'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
                    'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
                     'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
                   'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
