from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from .models import Book, Library, Author
from django.contrib.auth.forms import UserCreationForm

# Function-based view to list all books with plain text response
def list_books(request):
    books = Book.objects.all()
    # Create a simple text response
    response_text = "Books Available:\n"
    for book in books:
        authors = ", ".join([author.name for author in book.authors.all()])
        response_text += f"- {book.title} by {authors}\n"
    return HttpResponse(response_text, content_type="text/plain")

# HTML version of the list_books view
def list_books_html(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add books in this library to the context
        context['books'] = self.object.books.all()
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})