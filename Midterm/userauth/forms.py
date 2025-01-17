from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserEditForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']