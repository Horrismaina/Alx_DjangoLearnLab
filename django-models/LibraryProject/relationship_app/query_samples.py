import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment to use models in this script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"Author named {author_name} does not exist."

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"Library named {library_name} does not exist."

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return f"Either library named {library_name} or its librarian does not exist."

# Sample usage
if __name__ == "__main__":
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    print(f"Books by {author_name}: {books_by_author(author_name)}")

    # List all books in a library
    library_name = "Central Library"
    print(f"Books in {library_name}: {books_in_library(library_name)}")

    # Retrieve the librarian for a library
    print(f"Librarian for {library_name}: {librarian_for_library(library_name)}")
