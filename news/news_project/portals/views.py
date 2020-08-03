from django.core.paginator import Paginator
from django.shortcuts import render

from categories.models import Category
from articles.models import Article
from comments.forms import CommentForm


def _paginate(request, obj):
    paginator = Paginator(obj, 3)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    return paged_articles


def portal_page(request):
    categories = Category.objects.all()
    articles = Article.objects.order_by('-input_date').all()
    paged_articles = _paginate(request, articles)

    context = {
        "title": "Portal daffa news",
        "categories": categories,
        "articles": paged_articles,
    }
    return render(request, 'portal.html', context)


def archive_page(request, slug):
    categories = Category.objects.all()
    articles = Article.objects.order_by('-input_date').filter(category__slug__iexact=slug).filter(status='1')
    paged_articles = _paginate(request, articles)

    context = {
        "title": "Category: " + slug,
        "categories": categories,
        "articles": paged_articles,
    }
    return render(request, 'portal.html', context)


def author_page(request, author):
    categories = Category.objects.all()
    articles = Article.objects.order_by('-input_date').filter(user_input__username__iexact=author).filter(status='1')
    paged_articles = _paginate(request, articles)

    context = {
        "title": "Author: " + author,
        "categories": categories,
        "articles": paged_articles,
    }
    return render(request, 'portal.html', context)


def single_page(request, slug):
    categories = Category.objects.all()
    articles = Article.objects.filter(slug__iexact=slug).first()
    prev = Article.objects.filter(category__slug__iexact=articles.category.slug,slug__gt=articles.slug).order_by('slug').first()
    next = Article.objects.filter(category__slug__iexact=articles.category.slug,slug__lt=articles.slug).order_by('-slug').first()
    form = CommentForm(request.POST or None)
    # print(next.slug)
    context = {
        "title": articles.title,
        "categories": categories,
        "article": articles,
        "prev":prev,
        "next":next,
        "form":form,
    }
    return render(request, 'single.html', context)
