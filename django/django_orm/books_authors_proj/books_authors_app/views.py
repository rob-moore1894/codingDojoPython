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
        'otherAuthors': bookAuthors
    }
    return render(request, "book.html", context)

def addAuthorToBook(request, bookId):
    print(request.POST) #I get the id of the author
    this_author = Author.objects.get(id = request.POST['authorInfo'])
    this_book = Book.objects.get(id=bookId)

    this_book.authors.add(this_author)
    return redirect(f'/books/{bookId}')

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def addAuthor(request):
    newAuthor = Author.objects.create(first_name= request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    newAuthor.save()
    return redirect('/authors')

def showAuthor(request, authorId):
    authorToShow = Author.objects.get(id = authorId)
    authorBook = Book.objects.exclude(id = authorToShow.id)
    context = {
        'identifiedAuthor': authorToShow,
        'all_books': Book.objects.all(),
        'otherBooks': authorBook
    }
    return render(request,"author.html", context)

def addBookToAuthor(request, authorId):
    this_book = Book.objects.get(id = request.POST['bookInfo'])
    this_author = Author.objects.get(id = authorId)

    this_author.book.add(this_book)
    return redirect(f'/author/{authorId}')