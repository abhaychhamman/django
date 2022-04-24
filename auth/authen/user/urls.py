 
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',  views.register,name='register'),
    path('profile/',  views.profile,name='register'),
    path('login/',  views.login_page,name='register'),
    path('logout/',  views.logout_page,name='register'),
 
]
