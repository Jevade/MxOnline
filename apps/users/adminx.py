# -*- coding:utf-8 -*-
__author__ = 'Jevade'
__data__ = '2017/5/20 10:27'

from datetime import datetime

import xadmin
from xadmin import views
from django.db import models

from .models import EmailVertifyRecoder, Banner


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GloableSettings(object):
    site_title = "Jevade"
    site_footer = "JEVADE.LTD"
    menu_style = "accordion"


class EmailVertifyRecoderAdmin(object):
    list_display = ['code', 'email', 'send_time', 'send_type']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_time', 'send_type']
    pass


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVertifyRecoder, EmailVertifyRecoderAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GloableSettings)
