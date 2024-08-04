from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('brand/<slug:brand_slug>/', views.homepage, name='brand_wise_carlist'),
    path('car/details/<int:id>/', views.CarDetailView.as_view(), name='car_detail'),
    path('car/buy/<int:id>/', views.buy_car, name='buy_car'),
]
