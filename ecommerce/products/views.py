from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
from products.models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    def get_queryset(self):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
        queryset = Product.objects.featured()
        template_name = "products/detail_featured.html"

class ProductListView(ListView):
    template_name = "products/list.html"

    # cara 1
    # queryset = Product.objects.all()
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    # cara 2
    def get_queryset(self):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, 'products/list.html', context)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not found..')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('uh...')

        return instance

class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    # cara 1
    # queryset = Product.objects.all()
    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    # cara 2
    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404('product does not exists')
    #     return instance

    # cara 3
    def get_queryset(self):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kwargs):
    # cara 1
    # instance = Product.objects.get(pk=pk)

    # cara 2
    # instance = get_object_or_404(Product, pk=pk)  cara 2

    # cara 3
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print ("no such product")
    #     raise Http404('product does not exists')

    # cara 4
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404('product does not exists')

    # cara 5
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404('product does not exists')

    context = {
        'object':instance
    }
    return render(request, 'products/detail.html', context)