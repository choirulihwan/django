from django.urls import path

from .views import portal_page, archive_page, single_page, author_page

urlpatterns = [
    path('', portal_page, name='portal'),
    path('portal/cat/<slug:slug>', archive_page, name='archive'),
    path('portal/<slug:slug>', single_page, name='single'),
    path('portal/author/<str:author>', author_page, name='author')

]

app_name = 'portals'
