from django.urls import path
from .views import createText, register, login_view, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('manual/connect/', createText, name='create_textmodel'),
    path('login/', login_view, name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
