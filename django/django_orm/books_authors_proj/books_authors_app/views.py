from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "all_books":Book.objects.all()
    }
    return render(request,"index.html", context)

def addBook(request):
    newBook = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    newBook.save()
    return redirect('/')

def showBook(request, bookId):
    bookToShow = Book.objects.get(id=bookId)
    bookAuthors = Author.objects.exclude(book = bookToShow)
    context = {
        'identifiedBook': bookToShow,
        'all_authors': Author.objects.all(),
        'identifiedAuthors': bookAuthors
    }
    return render(request, "book.html", context)

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)