from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from home.models import *
from django.contrib import messages

# Create your views here.
def entryPage(request):
    return render(request, 'entryPage.html')

def studentLogin(request):
    return render(request, 'studentLogin.html')

def studentDashboard(request):
    return render(request, 'studentDashboard.html')

def adminDashboard(request):
   
    return render(request, 'adminDashboard.html')

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #user = adminidpassword.objects.check(adminid=username, adminpassword=password)
        user = adminidpassword.objects.all()
        user.filter(adminid = username, adminpassword = password)
        if user is not None:
            return redirect('/adminDashboard')
        else:
            return redirect('/adminLogin')
    
    return render(request, 'adminLogin.html')
    
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")
    
def documentation(request):
    return render(request, 'studentDocumentation.html')

def faqs(request):
    return render(request, 'studentFaqs.html')

def about(request):
    return render(request, 'studentAbout.html')

def contact(request):
    return render(request, 'studentContact.html')

def adminDocumentation(request):
    return render(request, 'adminDocumentation.html')

def adminFaqs(request):
    return render(request, 'adminFaqs.html')

def adminAbout(request):
    return render(request, 'adminAbout.html')

def adminContact(request):
    return render(request, 'adminContact.html')
