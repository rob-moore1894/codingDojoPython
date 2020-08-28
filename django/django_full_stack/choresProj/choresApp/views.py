from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users, Child, Chores
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    regValidation = Users.objects.regValidator(request.POST)
    print(regValidation)
    if len(regValidation) > 0:
        for value in regValidation.values():
            messages.error(request, value)
        return redirect('/')
    else: 
        hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        newUser = Users.objects.create(name=request.POST['name'], email=request.POST['email'], password=hashedpw)
        request.session['loggedInId'] = newUser.id
    return redirect("/user")

def login(request):
    loginValidation = Users.objects.loginValidator(request.POST)
    print(loginValidation)
    if len(loginValidation) > 0:
        for value in loginValidation.values():
            messages.error(request, value)
        return redirect('/')
    return redirect("/user")

def userPage(request):
    context = {
        'loggedInUser': Users.objects.get(id=request.session['loggedInId']),
        
    }
    return render(request, "user.html", context)