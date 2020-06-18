from django.urls import path

from .views import ReferenceListView

urlpatterns = [
    path('', ReferenceListView.as_view(), name='list'),
    # path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),

]

app_name = 'references'
