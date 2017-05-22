# -*- coding:utf-8 -*-
__author__ = 'Jevade'
__data__ = '2017/5/21 16:59'

from random import Random
from datetime import datetime

from django.core.mail import send_mail

from MxOnline.settings import EMAIL_FROM
from users.models import EmailVertifyRecoder


def random_str(random_length=8):
    str = ''
    chars = reduce(lambda x, y: x + y, [chr(i) + chr(i + 32) for i in range(65, 91)])
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    code = random_str(16)
    # user_profile = UserProfile(is_active=False, username=user_name, email=user_name,
    #                            password=make_password(pass_word))
    # user_profile.save()
    email_record = EmailVertifyRecoder(email=email, code=code, send_type=send_type)
    email_record.save()
    try:
        email_record.save()
    except:
        print('save error')
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return True
        else:
            return False
    elif send_type == "forget":
        email_title = "重置密码链接"
        email_body = "请点击下面的链接：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return True
        else:
            return False

