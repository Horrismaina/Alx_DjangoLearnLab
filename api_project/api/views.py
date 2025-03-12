from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ListAPIView for the previous task
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Define BookViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


    """
Authentication and Permissions:
- This API uses Token Authentication for all requests.
- Users must obtain a token by posting their username and password to /api-token-auth/.
- Include the token in the Authorization header of your requests.
"""

