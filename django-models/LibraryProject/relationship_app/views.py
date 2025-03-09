from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Function-based view to list all books
@login_required
def list_books(request):
    books = Book.objects.all()  # Query to get all books
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

# Class-based view to list all libraries
class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = 'list_libraries.html'
    context_object_name = 'libraries'

# Registration view for users
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
