from django import forms

# Django form
class ContactForm(forms.Form):
    fullname = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Your fullname"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email"
            }
        )
    )

    content = forms.CharField(
        min_length=10,
        label="Your message",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email harus gmail.com")
        return email