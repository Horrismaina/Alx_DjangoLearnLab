from django.db import models

# Author model: Represents a book author.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model: Represents a book written by an author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # A book is written by one author.

    def __str__(self):
        return self.title

# Library model: Represents a library that contains books.
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  # A library can have many books.

    def __str__(self):
        return self.name

# Librarian model: Represents the librarian assigned to a specific library.
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # Each library has one librarian.

    def __str__(self):
        return self.name
