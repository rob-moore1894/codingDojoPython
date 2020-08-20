from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('books/<int:bookId>', views.showBook),
    path('authors', views.authors),
]