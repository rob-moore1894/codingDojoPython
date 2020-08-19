from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "all_dojos":Dojo.objects.all(),
        "all_ninjas":Ninja.objects.all()
    }
    return render(request, "index.html", context)

def add_dojo(request):
    newDojo = Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    newDojo.save()
    return redirect("/")

def add_ninja(request):
    newNinja = Ninja.objects.create(dojo = Dojo.objects.get(id=request.POST['dojo']), first_name = request.POST['first_name'], last_name = request.POST['last_name'])
    newNinja.save()
    return redirect("/")
