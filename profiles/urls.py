from .views import *
from django.urls import path

urlpatterns = [
    path('', plogin, name='plogin'),
    path('home', home, name='home'),
    path('logoutuser', logoutuser, name='logoutuser'),
    path('registration', registration, name='registration'),
    ]