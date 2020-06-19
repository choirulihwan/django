from django import forms

class CategoryForm(forms.Form):
    cat_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category name..'})
    )