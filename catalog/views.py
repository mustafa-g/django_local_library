from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # count of objects
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_book_instances = BookInstance.objects.count()
    num_book_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_genre =  Genre.objects.count()
    num_book_white = Book.objects.filter(title__contains="White").count()

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_book_instances": num_book_instances,
        "num_book_instances_available": num_book_instances_available,
        "num_genre": num_genre,
        "num_book_white": num_book_white,
    }

    return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):
    model = Book


class  BookDetailView(generic.DetailView):
    model = Book