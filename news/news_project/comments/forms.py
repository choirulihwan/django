from django import forms
from tinymce.widgets import TinyMCE


class CommentForm(forms.Form):
    content = forms.CharField(
        label="Comments",
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30, "style": "resize: none"}),
        # disabled=True,
        # widget=forms.Textarea
    )

