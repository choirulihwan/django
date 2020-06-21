from django.urls import path

from .views import article_add, article_page, article_delete, article_update

urlpatterns = [
    path('', article_page, name='list'),
    path('add/', article_add, name='add'),
    path('update/<int:pk>', article_update, name='update'),
    path('delete/<int:pk>', article_delete, name='delete'),
    # path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),

]

app_name = 'articles'
