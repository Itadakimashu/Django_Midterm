from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name = 'add_album'),
    path('delete/<int:id>', views.AlbumDeleteView.as_view() , name = 'delete_album'),
    path('edit/<int:id>', views.AlbumEditView.as_view(), name = 'edit_album'),
]
