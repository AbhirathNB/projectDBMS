from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.entryPage, name= 'entryPage'),
    path("studentLogin", views.studentLogin, name = 'studentLogin'),
    path("adminLogin", views.adminLoginPage, name = 'adminLogin'),
    path("about", views.about, name = 'about'),
    path("contact", views.contact, name = 'contact'),
    path("documentation", views.documentation, name = 'documentation'),
    path("faqs", views.faqs, name = 'faqs'),
    path("studentDashboard", views.studentDashboard, name = 'studentDashboard'),
    path("adminDashboard", views.adminDashboard, name = 'adminDashboard'),
    path("adminAbout", views.adminAbout, name = 'adminAbout'),
    path("adminContact", views.adminContact, name = 'adminContact'),
    path("adminDocumentation", views.adminDocumentation, name = 'adminDocumentation'),
    path("adminFaqs", views.adminFaqs, name = 'adminFaqs'),
    path("previousResults", views.previousResults, name = 'previousResults'),
    path("viewRank", views.viewRank, name = 'viewRank'),
    path("attemptExam", views.attemptExam, name = 'attemptExam'),
    path("manageStudents", views.manageStudents, name = 'manageStudents'),
    path("createExam", views.createExam, name = 'createExam'),
    
]