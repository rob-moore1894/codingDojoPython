from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('shows', views.allShows),
    path('shows/new', views.newShowPage),
    path('shows/createShow', views.createShow),
    path('shows/<int:showId>', views.oneShow),
    path('shows/<int:showId>/edit', views.editShowPage),
    path('shows/<int:showId>/editShow', views.editShow),
    path('shows/<int:showId>/destroy', views.destroy)
]