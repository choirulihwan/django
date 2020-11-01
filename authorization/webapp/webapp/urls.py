"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import listing, single, request_info, user_info, private_page, staff_page, add_messages

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", listing, name="listing"),
    path("single/<int:blog_id>/", single, name="single"),
    path("req_info", request_info, name="req_info"),
    path("user_info", user_info, name="user_info"),
    path("private_page", private_page, name="private_page"),
    path("staff_page", staff_page, name="staff_page"),
    path("add_messages", add_messages, name="add_messages"),
    path("accounts/", include("django.contrib.auth.urls")),
]
