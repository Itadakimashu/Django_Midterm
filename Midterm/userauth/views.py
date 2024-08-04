from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.models import User

from django.views.generic import UpdateView

# from django.contrib.auth import login,logout,authenticate

from .forms import UserSignupForm,UserEditForm

# Create your views here.
def signup(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully.')
            return redirect('login')
        
    return render(request, 'user/signup.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm

    def get_success_url(self): 
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self): 
        return reverse_lazy('home')
    

@method_decorator(login_required, name='dispatch')
class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user/user_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)
    
    