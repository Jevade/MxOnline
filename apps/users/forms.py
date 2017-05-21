# -*- coding:utf-8 -*-
__author__ = 'Jevade'
__data__ = '2017/5/20 18:06'

from django import forms

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=3)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u"验证码错误"})
    password = forms.CharField(required=True, min_length=8)
