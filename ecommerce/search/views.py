from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = "search/view.html"

    # dipanggil ketika ada keyword pencarian
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    # dipanggil jika tdk ada query set
    # cara 2
    def get_queryset(self):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q') #get dict value using get
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()
