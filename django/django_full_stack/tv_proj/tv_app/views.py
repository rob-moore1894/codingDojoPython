from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from .models import Shows

# Create your views here.
def index(request):
    return redirect("/shows")

def newShowPage(request):
    return render(request, "new-show.html")

def createShow(request):
    print(request.POST)
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
    if len(request.POST['inputShowTitle']) > 0:
        this_show.title = request.POST['inputShowTitle']
    if len(request.POST['inputShowNetwork']) > 0:
        this_show.network = request.POST['inputShowNetwork']
    if len(request.POST['inputReleaseDate']) > 0:
        this_show.releaseDate = request.POST['inputReleaseDate']
    if len(request.POST['inputShowDesc']) > 0:
        this_show.description = request.POST['inputShowDesc']
    this_show.save()
    return redirect(f"/shows/{showId}")

def destroy(request, showId):
    this_show = Shows.objects.get(id=showId)
    this_show.delete()
    return redirect("/shows")

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response