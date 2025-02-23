# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return None

def list_library_books(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

def get_library_librarian(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None

# Example usage:
def run_sample_queries():
    # Create sample data
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter 1", author=author)
    book2 = Book.objects.create(title="Harry Potter 2", author=author)
    
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)
    
    librarian = Librarian.objects.create(name="John Doe", library=library)
    
    # Run queries
    print("Books by J.K. Rowling:")
    for book in query_books_by_author("J.K. Rowling"):
        print(f"- {book.title}")
    
    print("\nBooks in Central Library:")
    for book in list_library_books("Central Library"):
        print(f"- {book.title}")
    
    print("\nLibrarian at Central Library:")
    librarian = get_library_librarian("Central Library")
    if librarian:
        print(f"- {librarian.name}")

if __name__ == "__main__":
    run_sample_queries()