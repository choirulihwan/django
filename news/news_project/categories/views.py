from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.views.generic import ListView
from .models import Category
from .forms import CategoryForm
from news_project.utils import generate_sidebar


@login_required(login_url='/login')
def category_page(request):
    parent_menu = generate_sidebar(request)
    categories = Category.objects.all()

    context = {
        "title": "Categories",
        "parent_menu": parent_menu,
        'object_list': categories,
    }
    return render(request, 'list_category.html', context=context)


@login_required(login_url='/login')
@permission_required('categories.delete_category')
def category_delete(request, pk):
    Category.objects.filter(pk=pk).delete()
    messages.success(request, "Category is deleted")
    return HttpResponseRedirect('/categories')


@login_required(login_url='/login')
@permission_required('categories.add_category')
def category_add(request, pk=None):
    parent_menu = generate_sidebar(request)
    if pk is None:
        cat_form = CategoryForm(request.POST or None)
        title = "Add"
    else:
        categories = Category.objects.filter(pk=pk).first()
        cat_form = CategoryForm(request.POST or None, initial={'cat_name': categories})
        title = "Update"

    context = {
        "title": title + " category",
        "parent_menu": parent_menu,
        "form": cat_form
    }

    # return HttpResponse(str(pk))

    if cat_form.is_valid():
        cat_name = cat_form.cleaned_data.get('cat_name')
        if pk is None:
            Category.objects.create(cat_name=cat_name)
        else:
            obj = Category.objects.get(pk=pk)
            obj.cat_name = cat_name
            obj.save()

        messages.success(request, "Category is saved sucessfully")
        return HttpResponseRedirect('/categories')

    return render(request, 'form_category.html', context=context)


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

