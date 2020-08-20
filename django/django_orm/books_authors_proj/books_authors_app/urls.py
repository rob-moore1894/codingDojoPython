from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('books/<int:bookId>', views.showBook),
    path('addAuthorToBook/<int:bookId>', views.addAuthorToBook),
    path('authors', views.authors),
    path('addAuthor', views.addAuthor),
    path('authors/<int:authorId>', views.showAuthor),
    path('addBookToAuthor/<int:authorId', views.addBookToAuthor),
]