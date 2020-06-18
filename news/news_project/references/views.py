from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

class ReferenceListView(ListView):
    template_name = "references/list.html"