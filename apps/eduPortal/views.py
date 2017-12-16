from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "eduPortal/login.html")

def login(request):

    return redirect('/eduPortal/dashboard')

def register(request):

    if request.method == "POST":
        print "got a post command"
        result = User.objects.validate_registration(request.POST)
        if type(result) == list:
            for x in result:
                messages.error(request, x)
                return redirect('/')
        else:
            request.session['id'] = result.id
            request.session['name'] = request.POST['name']
            messages.success(request, 'You have registered successfully!')
            return render('/eduProtal/register.html')

def dashboard(request):
    return render(request, "eduPortal/dashboard.html")

# this request takes user from register page to dashboard page once all the info is given
def registerSubmit(request):

    return redirect('eduPortal/dashboard')

# this request takes user from dashboard to hangouts page
def connect(request):
    return render(request, "eduPortal/hangouts.html")

# this request takes user from dashboard page to connections page
def findPartner(request):
    return render(request, "eduPortal/connections.html")