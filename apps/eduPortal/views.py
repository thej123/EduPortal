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
        
        request.session['id'] = result.id
        request.session['name'] = result.name
        request.session['role'] = result.role
        print 'login success', request.session['role'], result.role
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
            request.session['role'] = request.POST['role']
            messages.success(request, 'You have registered successfully!')
            return redirect('/eduPortal/registerPage')

def logout(request):
    return redirect("/")

def dashboard(request):
    topics = User.objects.get(id=request.session['id']).topics
    print "got topics?", topics
    return render(request, "eduPortal/dashboard.html")

def dashboardTwo(request):
    context = {
        "students": User.objects.filter(role = "student"),
        "teachers": User.objects.filter(role = "teacher")
        }
    user = User.objects.get(id=request.session['id'])
    print "inside server, dashbaord two, time", user.time
    print "inside server, dashbaord two, topics", user.topics
    return render(request, "eduPortal/dashboard2.html", context)

def studySession(request):
    context = {
        "students": User.objects.filter(role = "student"),
        "teachers": User.objects.filter(role = "teacher")
        }
    user = User.objects.get(id=request.session['id'])
    return render(request, "eduPortal/studySession.html", context)

def register(request):
    print request.session['id'], request.session['name']
    user = User.objects.get(id=request.session['id'])
    print "inside server, register, time", user.time
    print "inside server, register, topics", user.topics
    return render(request, "eduPortal/register.html")

# this request takes user from register page to dashboard page once all the info is given
def registerSubmitInRegisterPage(request):
    
    print request.POST
    if "subject" in request.POST:
        User.objects.get(id=request.session['id']).topics.append(request.POST['subject'])
    if "saturdayTime" in request.POST:
        User.objects.get(id=request.session['id']).time['saturday'].append(request.POST['saturdayTime'])
    if "sundayTime" in request.POST:    
        User.objects.get(id=request.session['id']).time['sunday'].append(request.POST['sundayTime'])
    if "mondayTime" in request.POST:  
        User.objects.get(id=request.session['id']).time['monday'].append(request.POST['mondayTime'])
    if "tuesdayTime" in request.POST:  
        User.objects.get(id=request.session['id']).time['tuesday'].append(request.POST['tuesdayTime'])
    if "wednesdayTime" in request.POST:  
        User.objects.get(id=request.session['id']).time['wednesday'].append(request.POST['wednesdayTime'])
    if "thursdayTime" in request.POST:  
        User.objects.get(id=request.session['id']).time['thursday'].append(request.POST['thursdayTime'])
    if "fridayTime" in request.POST:  
        User.objects.get(id=request.session['id']).time['friday'].append(request.POST['fridayTime'])
    return redirect('/eduPortal/dashboardTwo')

# this request takes user from dashboard to hangouts page
def connect(request):
    return render(request, "eduPortal/hangouts.html")

# this request takes user from dashboard page to connections page
def findPartner(request):
    return render(request, "eduPortal/connections.html")