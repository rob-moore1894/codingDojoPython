from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
]

from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")