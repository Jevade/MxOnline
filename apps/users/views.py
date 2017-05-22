# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
# Create your views here.

from .models import UserProfile, EmailVertifyRecoder
from forms import LoginForm, RegisterForm, ForgetForm
from utils.email_send import send_register_email


class MyBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            if user.check_password(password):
                return user
            else:
                return UserProfile(nick_name="None")
        except Exception as e:
            return None


class ForgetView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            user_name = request.POST.get("email", "")
            user_find = UserProfile.objects.filter(email=user_name)
            if user_find:
                status = send_register_email(user_name, "forget")
                if status:
                    return render(request, "forgetpwd.html", {"msg": "邮件已发送"})
                else:
                    return render(request, "forgetpwd.html", {"msg": "邮件发送失败"})
            else:
                return render(request, "forgetpwd.html", {"msg": "用户不存在"})

            pass
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})

    pass


class ResetPassword(View):
    def get(self, request, reset_code):
        return render(request, "password_reset.html", {"reset_code": reset_code})

    def post(self, request):
        reset_code = request.POST.get("reset_code", "")
        all_records = EmailVertifyRecoder.objects.filter(code=reset_code[:-1])
        if all_records:
            email = all_records[0].email
        else:
            return render(request, "forgetpwd.html", {"msg": u"链接已失效"})
        all_records = EmailVertifyRecoder.objects.filter(email=email)
        pass_word1 = request.POST.get("password", "")
        pass_word2 = request.POST.get("password2", "")
        if pass_word1 != pass_word2:
            return render(request, "forgetpwd.html", {"msg": u"不一致"})
        set = False
        if all_records:
            for record in all_records:
                if not set:
                    email = record.email
                    user = UserProfile.objects.get(email=email)
                    user.password = make_password(pass_word1)
                    user.save()
                    set = True
                record.delete()
            return render(request, "login.html", {"msg": u"密码已更改，重新登录"})
        return render(request, "forgetpwd.html")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass_word = request.POST.get("password", "")
            user_name = request.POST.get("email", "")
            user_find = UserProfile.objects.filter(email=user_name)
            if user_find:
                return render(request, "login.html", {"msg": "用户已存在,请登录"})
            user_profile = UserProfile(is_active=False, username=user_name, email=user_name,
                                       password=make_password(pass_word))
            user_profile.save()
            try:
                user_profile.save()
            except:
                print("save error")
            finally:
                send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVertifyRecoder.objects.filter(code=active_code[:-1])
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                record.delete()
            return render(request, "login.html", {"msg": u"已激活"})
        return render(request, "login.html")

        pass


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:

                if user.nick_name == "None":
                    return render(request, "login.html", {"msg": "密码错误！"})
                else:
                    if user.is_active:
                        login(request, user)  # 在request写入信息，
                        return render(request, "index.html")
                    else:
                        return render(request, "login.html", {"msg": "用户未激活！"})

            else:
                return render(request, "login.html", {"msg": "用户名错误！"})

        else:
            return render(request, "login.html", {"login_form": login_form})


def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            if user.nick_name == "None":
                return render(request, "login.html", {"msg": "密码错误！"})
            else:
                login(request, user)  # 在request写入信息，
                return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名错误！"})
        pass
    elif request.method == "GET":
        return render(request, 'login.html', {})
