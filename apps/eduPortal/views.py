from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "eduPortal/login.html")

def loginSubmit(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for x in result:
            messages.error(request, x)
        return redirect('/')
    else:
        print 'login success', result
        request.session['id'] = result.id
        messages.success(request, 'You have logged in!')
        return redirect('/eduPortal/dashboard')

def registerSubmit(request):
    if request.method == "POST":
        result = User.objects.validate_registration(request.POST)
        if type(result) == list:
            for x in result:
                messages.error(request, x)
                return redirect('/')
        else:
            request.session['id'] = result.id
            request.session['name'] = request.POST['name']
            messages.success(request, 'You have registered successfully!')
            return redirect('/eduPortal/registerPage')

def dashboard(request):
    return render(request, "eduPortal/dashboard.html")

def register(request):
    return render(request, "eduPortal/register.html")

# this request takes user from register page to dashboard page once all the info is given
def registerSubmitTwo(request):

    return redirect('eduPortal/dashboard')

# this request takes user from dashboard to hangouts page
def connect(request):
    return render(request, "eduPortal/hangouts.html")

# this request takes user from dashboard page to connections page
def findPartner(request):
    return render(request, "eduPortal/connections.html")