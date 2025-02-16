from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()books = Book.objects.all()
print(f"Number of books in database: {len(books)}")
try:
    Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book was successfully deleted.")


<!-- Number of books in database: 0 -->