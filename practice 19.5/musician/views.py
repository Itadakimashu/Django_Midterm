from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView,UpdateView

from .forms import MusicianForm
from .models import Musician

@method_decorator(login_required,name = 'dispatch')
class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/add_musician.html'
    
    success_url = reverse_lazy('home')

@method_decorator(login_required,name = 'dispatch')
class MusicianEditView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/edit_musician.html'
    pk_url_kwarg = 'id'

    success_url = reverse_lazy('home')