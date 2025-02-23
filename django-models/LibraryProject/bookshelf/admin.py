from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search capability for these fields
    search_fields = ['title', 'author']
    
    # Add filter options in the right sidebar
    list_filter = ('publication_year', 'author')
    
    # Add field ordering
    ordering = ('title',)
