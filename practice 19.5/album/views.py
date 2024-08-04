from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView,UpdateView,DeleteView

from .forms import AlbumForm
from .models import Album

@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/add_album.html'

    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class AlbumDeleteView(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/delete.html'

    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'album/edit_album.html'

    success_url = reverse_lazy('home')

