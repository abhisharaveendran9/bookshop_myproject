from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})
        }