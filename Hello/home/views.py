from asyncio.windows_events import NULL
#from typing_extensions import Self
from django.db import connection
from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from home.models import *
from django.contrib import messages

# Create your views here.
def entryPage(request):
    return render(request, 'entryPage.html')

def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = studentidpassword.objects.raw(
        f"SELECT * FROM home_studentidpassword WHERE studentid_id='{username}' and studentpassword = '{password}'"
    )

        if len(user) != 0:

            return redirect('/studentDashboard')
        else:
            return redirect('/studentLogin')
          
    return render(request, 'studentLogin.html')

def studentDashboard(request):
    return render(request, 'studentDashboard.html')

def adminDashboard(request):
   
    return render(request, 'adminDashboard.html')

def adminLoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = adminidpassword.objects.raw(
        f"SELECT * FROM home_adminidpassword WHERE adminid_id='{username}' and adminpassword = '{password}'"
    )

        if len(user) != 0:

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

def previousResults(request):
    return render(request, 'previousResults.html')

def viewRank(request):
    return render(request, 'viewRank.html')

def attemptExam(request):
    return render(request, 'attemptExam.html')

def manageStudents(request):
    return render(request, 'manageStudents.html')

def createExam(request):
    return render(request, 'createExam.html')

