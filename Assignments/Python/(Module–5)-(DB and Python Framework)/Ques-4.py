# Q.4 What is Django URLs?make program to create django urls

"""
In django,URL(uniform resource locators) are used to map URL patterns to views in our application

It allows to specify what code should run when user visits URL on our website

configuration is defined in urls.py

"""
# in our app / views.py

from django.http import HttpResponse

def login(request):
    return HttpResponse("This is login page")

def dashboard(request):
    return HttpResponse("This is dashboard page")

def logout(request):
    return HttpResponse("This is logout page")


# in out app / urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]