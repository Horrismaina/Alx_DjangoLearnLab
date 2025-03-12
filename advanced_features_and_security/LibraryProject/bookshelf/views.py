from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
@csrf_protect  # Ensuring CSRF protection for form submission
def book_create(request):
    if request.method == "POST":
        # Process form submission securely
        pass
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
@csrf_protect  # Ensuring CSRF protection
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # Process form submission securely
        pass
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
@csrf_protect  # CSRF protection on delete
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

