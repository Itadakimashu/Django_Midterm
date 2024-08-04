from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login_req, name='login'),
    path('logout/', views.logout_req, name = 'logout'),
    path('change_password/',views.change_password, name = 'change_password'),
    path('forgot_password/', views.change_pass_without_old, name = 'change_pass_without_old'),
    path('user_edit/' , views.user_edit, name = 'user_edit'),
    path('profile/', views.profile, name = 'profile')
]
