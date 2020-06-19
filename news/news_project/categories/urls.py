from django.urls import path

from .views import category_page, category_add, category_delete

urlpatterns = [
    path('', category_page, name='list'),
    path('add/', category_add, name='add'),
    path('update/<int:pk>', category_add, name='update'),
    path('delete/<int:pk>', category_delete, name='delete'),
    # path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),

]

app_name = 'categories'
