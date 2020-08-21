from django.shortcuts import render, redirect
from .models import Shows
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect("/shows")

def newShowPage(request):
    return render(request, "new-show.html")

def createShow(request):
    print(request.POST)
    errorsFound = Shows.objects.showValidator(request.POST)
    if len(errorsFound) > 0:
        for value in errorsFound.values():
            messages.error(request, value)
        return redirect("/shows/new")
    newShow = Shows.objects.create(title = request.POST['inputShowTitle'], network = request.POST['inputShowNetwork'], releaseDate= request.POST['inputReleaseDate'], description=request.POST['inputShowDesc'])
    newShow.save()
    return redirect(f"/shows/{newShow.id}")

def allShows(request):
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request,"all-shows.html", context)

def oneShow(request, showId):
    context = {
        "selectedShow": Shows.objects.get(id=showId),
    }
    return render(request, "one-show.html", context)

def editShowPage(request, showId):
    context = {
        "selectedShow": Shows.objects.get(id=showId),
    }
    return render(request, "update-show.html", context)
    
def editShow(request, showId):
    this_show = Shows.objects.get(id=showId)
    errorsFound = Shows.objects.showValidator(request.POST)
    if len(errorsFound) > 0:
        for value in errorsFound.values():
            messages.error(request, value)
        return redirect(f"/shows/{showId}/edit") 
    this_show.title = request.POST['inputShowTitle']
    this_show.network = request.POST['inputShowNetwork']
    this_show.releaseDate = request.POST['inputReleaseDate']
    this_show.description = request.POST['inputShowDesc']
    this_show.save()
    return redirect(f"/shows/{showId}")

def destroy(request, showId):
    this_show = Shows.objects.get(id=showId)
    this_show.delete()
    return redirect("/shows")
