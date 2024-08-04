from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView,LogoutView

# from django.contrib.auth import login,logout,authenticate

from .forms import UserSignupForm

# Create your views here.
def signup(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created Successfully.')
        
    return render(request, 'user/signup.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm

    def get_success_url(self): 
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self): 
        return reverse_lazy('home')