from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def homepage(request):
    context = {
        "title":"Homepage",
        "content": "Welcome to the homepage"
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
        if request.method == 'POST':
            # print(request.POST)
            print(request.POST.get('fullname'))
            print(request.POST.get('email'))
            print(request.POST.get('content'))



    return render(request, "contact/view.html", context)

def homepage_old(request):
    return HttpResponse("Hello world")
