from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class User_details_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

user_form=User_details_form()
