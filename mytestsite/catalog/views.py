from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Genre, Book, BookInstance, Author

def index(request):
    """View function for home page of site."""
    # Generate count of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    num_genre_african = Book.objects.filter(genre__name__icontains='African').count()
    num_novel_books = Book.objects.filter(summary__contains='novel').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre_african': num_genre_african,
        'num_novel_books': num_novel_books,
    }
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

# Implementing class based view as a function for boook detail
"""def book_detail_view(request, primary_key):
  try:
    book = Book.objects.get(pk=primary_key)
  except Book.DoesNotExist:
    raise Http404('Book does not exist')

  return render(request, 'catalog/book_detail.html', context={'book': book})
  """

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author