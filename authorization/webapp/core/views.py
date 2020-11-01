from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from core.models import Blog


def listing(request):
    data = {
        "blogs": Blog.objects.all(),
    }
    return render(request, 'listing.html', data)


def single(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        "blog": blog,
    }
    return render(request, "single.html", data)


def request_info(request):
    text = f"""
            Some attributes of the HttpRequest object:

            scheme: {request.scheme}
            path:   {request.path}
            method: {request.method}
            GET:    {request.GET}
            user:   {request.user}
        """
    return HttpResponse(text, content_type="text/plain")


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """
    return HttpResponse(text, content_type="text/plain")


@login_required
def private_page(request):
    return HttpResponse('member only, welcome ' + request.user.username, content_type="text/plain")


@user_passes_test(lambda user: user.is_staff)
def staff_page(request):
    return HttpResponse("Hi " + request.user.username + ", Staff must wash hands", content_type="text/plain")


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, f"Be Carefull")
    messages.add_message(request, messages.ERROR, f"STOP")
    return HttpResponse("messages added", content_type="text/plain")