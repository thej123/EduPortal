from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, "eduPortal/login.html")

def register(request):
    # if request.method == 'POST':
    #     request.session['name'] = request.POST['name']
    #     return redirect("/")
    # else:
    #     return redirect("/")
    return render(request, "eduPortal/register.html")

def dashboard(request):
    return render(request, "eduPortal/dashboard.html")
