
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaulttags import register

from .forms import LoginForm
from .utils import generate_sidebar

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    else:
        login_form = LoginForm(request.POST or None)
        class_body = "class='hold-transition login-page'"
        icon_list = ['glyphicon-envelope', 'glyphicon-lock']

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
        else:
            context = {
                "form": login_form,
                "class_body": class_body,
                "icon_list": icon_list,
                "title": "Login | DaffaNews"
            }

        return render(request, "auth/login.html", context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')


def dashboard_page(request):
    if request.user.is_authenticated:
        parent_menu = generate_sidebar(request)
        context = {
            "title": "Dashboard",
            "parent_menu": parent_menu,
        }
        return render(request, 'dashboard.html', context=context)
    else:
        return HttpResponseRedirect('/login')