from django.shortcuts import render

from .forms import LoginForm

def login_page(request):
    login_form = LoginForm(request.POST or None)
    class_body = "class='hold-transition login-page'"
    # icon_list = ['<span class="glyphicon glyphicon-envelope form-control-feedback"></span>',
    #              '<span class="glyphicon glyphicon-lock form-control-feedback"></span>']
    icon_list = ['glyphicon-envelope', 'glyphicon-lock']

    context ={
        "form":login_form,
        "class_body": class_body,
        "icon_list" : icon_list,
    }

    return render(request, "auth/login.html", context)