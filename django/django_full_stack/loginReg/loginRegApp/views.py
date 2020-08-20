from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt   

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    print(request.POST)
    validationErrors = User.objects.regValidator(request.POST)
    print(validationErrors)
    if len(validationErrors) > 0:
        for value in validationErrors.values():
            messages.error(request, value)
        return redirect('/')
    else:
        #encrypt the password first
        hashedPw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        newUser = User.objects.create(first_name = request.POST['fname'], email= request.POST['email'], password= hashedPw)
        request.session['loggedInId'] = newUser.id #cannot store entire User Object in this session

    return redirect('/home')

def home(request):
    context = {
        'loggedInUser': User.objects.get(id=request.session['loggedInId'])
    }
    return render(request, "home.html", context)