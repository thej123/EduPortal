from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
    request.session.clear()
    return render(request, "eduPortal/login.html")

def loginSubmit(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for x in result:
            messages.error(request, x)
        return redirect('/')
    else:
        print 'login success', type(result.topics)
        request.session['id'] = result.id
        request.session['name'] = result.name
        messages.success(request, 'You have logged in!')
        if not result.level:
            return redirect('/eduPortal/registerPage')
        else:
            return redirect('/eduPortal/dashboardTwo')

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

def logout(request):
    return redirect("/")

def dashboard(request):
    return render(request, "eduPortal/dashboard.html")

def dashboardTwo(request):
    context = {
        "results": User.objects.all()
        }
    print "inside server, dashbaord two", context['results']
    return render(request, "eduPortal/dashboard2.html", context)

def register(request):
    print request.session['id'], request.session['name']
    return render(request, "eduPortal/register.html")

# this request takes user from register page to dashboard page once all the info is given
def registerSubmitInRegisterPage(request):
    print request.POST
    User.objects.get(id=session['id']).topics.add(request.POST['topics'])
    return redirect('/eduPortal/registerPage')

# this request takes user from dashboard to hangouts page
def connect(request):
    return render(request, "eduPortal/hangouts.html")

# this request takes user from dashboard page to connections page
def findPartner(request):
    return render(request, "eduPortal/connections.html")