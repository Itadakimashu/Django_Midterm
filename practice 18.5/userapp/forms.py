from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name' ,'last_name','email', 'password1', 'password2')


class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name']