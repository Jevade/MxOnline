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
    email_record = EmailVertifyRecoder()
    code = random_str(16)
    email_record.email = email
    email_record.code = code
    email_record.send_type = send_type
    email_record.send_time = datetime.now
    try:
        email_record.save()
    except:
        print('save error')

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接：http://127.0.0.1:8000/active/{0}".format(str)
        send_status=send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
        else:
            return False
