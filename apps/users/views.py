# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import  make_password
# Create your views here.

from .models import UserProfile
from forms import LoginForm, RegisterForm
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



class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass_word = request.POST.get("password", "")
            user_name = request.POST.get("email", "")
            user_profile = UserProfile(username=user_name,email=user_name,password=make_password(pass_word))
            user_profile.save()
            try:
                user_profile.save()
            except:
                print("save error")
            finally:
                send_register_email(user_name,"register")

            # login(request, user_profile)  # 在request写入信息，
            return render(request, "index.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


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
                    login(request, user)  # 在request写入信息，
                    return render(request, "index.html")
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
