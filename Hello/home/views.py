from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from home.models import *
from django.contrib import messages

# Create your views here.
def entryPage(request):
    return render(request, 'entryPage.html')

def studentLogin(request):
    return render(request, 'studentLogin.html')

def adminLogin(request):
    return render(request, 'adminLogin.html')
    
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutpage")
