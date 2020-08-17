from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'counter' in request.session == 0:
        request.session['counter'] = 1
    else: 
        request.session['counter'] += 1
    return render(request, "index.html")

def destroy(request):
    request.session['counter'] = 0
    return redirect("/")

def add(request):
    request.session['counter'] += 1
    return redirect("/")