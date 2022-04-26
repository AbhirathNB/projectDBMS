from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.entryPage, name= 'entryPage'),
    path("studentLogin", views.studentLogin, name = 'studentLogin'),
    path("adminLogin", views.adminLogin, name = 'adminLogin'),
    path("about", views.about, name = 'about')
]