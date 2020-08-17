from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "date": strftime("%B %d, %Y", gmtime()),
        "time": strftime("%I:%M %p %z(UTC)", gmtime())
    }
    return render(request, "index.html", context)