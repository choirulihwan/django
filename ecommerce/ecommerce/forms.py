from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

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

    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your phone number"
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

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )

class RegisterForm(forms.Form):
        username = forms.CharField()
        email   = forms.EmailField()
        password = forms.CharField(
            widget=forms.PasswordInput
        )
        password2 = forms.CharField(
            widget=forms.PasswordInput,
            label="Password confirmation"
        )
        first_name = forms.CharField()
        last_name = forms.CharField(required=False)

        def clean_username(self):
            username = self.cleaned_data.get('username')
            qs = User.objects.filter(username=username)
            if qs.exists():
                raise forms.ValidationError("Username is taken")
            return username

        def clean_email(self):
            email = self.cleaned_data.get('email')
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("Email is taken")
            return email

        def clean(self):
            data = self.cleaned_data
            password = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('password2')
            if password != password2:
                raise forms.ValidationError("password must match")
            return data
