from django.shortcuts import render

# Create your views here.
from .models import Genre, Book, BookInstance, Author

def index(request):
    """View function for home page of site."""
    