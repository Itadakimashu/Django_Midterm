from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.MusicianCreateView.as_view(), name = 'add_musician'),
    path('edit/<int:id>',views.MusicianEditView.as_view(), name = 'edit_musician'),
]
