from django.shortcuts import render,redirect

from album.models import Album

def homepage(request):
    albums = Album.objects.all()
    return render(request, 'home.html',{'albums':albums})




