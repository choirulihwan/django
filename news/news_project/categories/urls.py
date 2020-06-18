from django.urls import path

from .views import category_page

urlpatterns = [
    path('', category_page, name='list'),
    path('update/<int:pk>', category_page, name='update'),
    path('delete/<int:pk>', category_page, name='delete'),
    # path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),

]

app_name = 'categories'
