from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, UserEditForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created Successfully Please Log In')
                form.save()
                return redirect('login')
        return render(request, 'signup.html', {'form' : form})
    else:
        messages.error(request, 'Logged in accounts cant create accounts')
        return redirect('home')


def login_req(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = name,password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfuly Logged In')
                    return redirect('home')
                else:
                    messages.error(request, form.errors)
                    redirect('login')
            else:
                messages.error(request, form.errors)
                redirect('login')
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    else:
        messages.error(request, 'You are Already logged in')
        return redirect('home')

def logout_req(request):
    logout(request)
    messages.success(request, 'Successfuly Logged Out')
    return redirect('home')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)# dont logout the user
            messages.success(request, 'Password Changed Successfully')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            
    form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form' : form})

@login_required
def change_pass_without_old(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)# dont logout the user
            messages.success(request, 'Password Changed Successfully')
            return redirect('home')
        else:
            messages.error(request, form.errors)
    form = SetPasswordForm(request.user)
    return render(request, 'change_password.html', {'form' : form})

    
@login_required
def user_edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            
    form = UserEditForm(instance=request.user)
    return render(request, 'user_edit.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'profile.html')
