from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.entryPage, name= 'entryPage'),
    path("studentLogin", views.studentLogin, name = 'studentLogin'),
    path("adminLogin", views.adminLogin, name = 'adminLogin'),
    path("about", views.about, name = 'about'),
    path("contact", views.contact, name = 'contact'),
    path("documentation", views.documentation, name = 'documentation'),
    path("faqs", views.faqs, name = 'faqs'),
    path("studentDashboard", views.studentDashboard, name = 'studentDashboard'),
    path("adminDashboard", views.adminDashboard, name = 'adminDashboard')
]