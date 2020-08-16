from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}")

def destroy(request, number):
    return redirect('/blogs')

def json(request):
    blog = {
        'title': 'Blog title',
        'content': 'Blog content'
    }
    return JsonResponse(blog)