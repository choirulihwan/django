from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Article
from .forms import ArticleForm
from news_project.utils import generate_sidebar


@login_required(login_url='/login')
def article_page(request):
    parent_menu = generate_sidebar(request)
    articles = Article.objects.all()

    context = {
        "title": "List articles",
        "parent_menu": parent_menu,
        'object_list': articles,
    }
    return render(request, 'list_article.html', context=context)


@login_required(login_url='/login')
@permission_required('articles.delete_article')
def article_delete(request, pk):
    Article.objects.filter(pk=pk).delete()
    messages.success(request, "Article is deleted")
    return HttpResponseRedirect('/articles')


def article_add_update(request, pk=None):
    parent_menu = generate_sidebar(request)
    if pk is None:
        form = ArticleForm(request.POST or None)
        title = "Add"
        image = ""
    else:
        articles = Article.objects.filter(pk=pk).first()
        form = ArticleForm(request.POST or None,
            initial= {
                'title': articles,
                'category': articles.category,
                'status': articles.status,
                'content': articles.content
                })
        title = "Update"
        image = articles.image


    context = {
        "title": title + " article",
        "parent_menu": parent_menu,
        "form": form,
        "image": image
    }

    # return HttpResponse(str(pk))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category = form.cleaned_data.get('category')
            content = form.cleaned_data.get('content')
            status = form.cleaned_data.get('status')
            user_input = request.user

            if request.FILES is not None:
                image = form.cleaned_data.get('image')
            else:
                image = ''

            if pk is None:
                Article.objects.create(title=title, category=category, content=content,
                                       status=status, image=image, user_input=user_input)

            else:
                obj = Article.objects.get(pk=pk)
                obj.title = title
                obj.category = category
                obj.content = content
                obj.status = status
                obj.user_update = request.user
                if image is not None:
                    obj.image = image
                obj.save()

            messages.success(request, "Article is saved sucessfully")
            return HttpResponseRedirect('/articles')

    return render(request, 'form_article.html', context=context)


@login_required(login_url='/login')
@permission_required('articles.add_article')
def article_add(request):
    return article_add_update(request)


@login_required(login_url='/login')
@permission_required('articles.change_article')
def article_update(request, pk):
    return article_add_update(request, pk)
