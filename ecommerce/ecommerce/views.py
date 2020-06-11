from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model

def homepage(request):
    # print(request.session.get('first_name'))
    context = {
        "title":"Homepage",
        "content": "Welcome to the homepage",
        "premium_content": "Yeaaaahhhh",
        "nama": request.session.get('first_name', 'Guest'),
    }
    return render(request, "homepage.html", context)

def about_page(request):
    context = {
        "title": "About page",
        "content": "Welcome to the about page"
    }
    return render(request, "homepage.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "Welcome to the contact page",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        # if request.method == 'POST':
        #     print(request.POST)
        #     print(request.POST.get('fullname'))
        #     print(request.POST.get('email'))
        #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form":login_form
    }
    print("user logged in")

    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('Login success')
            login(request, user)
        else:
            print('Error')
            #reset form
            context["form"] = LoginForm

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        new_user = User.objects.create_user(username=username, email=email,
                                            password=password, first_name=first_name, last_name=last_name)
        print(new_user)
        return HttpResponseRedirect('/register')
    return render(request, "auth/register.html", context)

def homepage_old(request):
    return HttpResponse("Hello world")
