from rest_framework import generics, filters
from django_filters import rest_framework as django_filters  # Ensure this import is included for filtering
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # Ensure this is exactly as required

# ListView: Retrieve all books with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Public read-only access, authenticated users can modify
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Enable filtering by title, author, and year
    search_fields = ['title', 'author__name']  # Enable search by title and author
    ordering_fields = ['title', 'publication_year']  # Enable ordering by title and publication year

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Public read-only access

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books



# BookListView: Handles retrieving all books
# Accessible by unauthenticated users for read-only access

# BookCreateView: Handles creating new books
# Accessible only by authenticated users

