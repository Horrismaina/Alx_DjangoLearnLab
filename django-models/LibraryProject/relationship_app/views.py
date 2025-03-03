from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query to get all books
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
