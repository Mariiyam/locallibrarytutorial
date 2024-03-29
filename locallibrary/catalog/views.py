from pyexpat import model
from unicodedata import name
from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact= 'a').count
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_books_engineering =  Book.objects.filter(title__iexact= 'engineering').count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors' : num_authors,
        'num_genres' : num_genres,
        'num_books_engineering': num_books_engineering,
    }
    
    
    return render(request, 'index.html', context= context)



class BookListView(generic.ListView):
    model= Book
    
    
class BookDetailView(generic.DetailView):
    model= Book
    

class AuthorListView(generic.ListView):
    model= Author
    
class AuthorDetailView(generic.DetailView):
    model= Author