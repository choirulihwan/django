from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Category
from news_project.utils import generate_sidebar

def category_page(request):
    if request.user.is_authenticated:
        parent_menu = generate_sidebar(request)
        categories = Category.objects.all()

        context = {
            "title": "Categories",
            "parent_menu": parent_menu,
            'object_list': categories
        }
        return render(request, 'list_category.html', context=context)
    else:
        return HttpResponseRedirect('/login')

# class CategoryListView(ListView):
#     template_name = "list_category.html"
#
#     def get_queryset(self):
#         request = self.request
#         return Category.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         request = self.request
#         context = super(CategoryListView, self).get_context_data(**kwargs)
#         parent_menu = generate_sidebar(request)
#         context['parent_menu'] = parent_menu
#         context['title'] = 'Categories'
#         return context

