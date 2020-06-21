from django import forms
from tinymce.widgets import TinyMCE

from .models import STATUS_CHOICES
from categories.models import Category


class ArticleForm(forms.Form):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput( attrs={'class':'form-control', 'placeholder':'title..'})
    )
    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'})
    )
    status = forms.CharField(
        label='Status',
        widget=forms.Select(choices=STATUS_CHOICES, attrs={'class':'form-control'})
    )
    content = forms.CharField(
        widget=TinyMCE()
    )
    image = forms.FileField(required=False)

