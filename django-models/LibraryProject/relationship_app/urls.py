from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books

urlpatterns = [
    # Home URL
    path('', views.list_books_html, name='home'),



    # List Books
    path('books/', views.list_books, name='list_books'),
  

    # Library Detail (class-based view)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User Registration
    path('register/', views.register, name='register'),

    # User Login and Logout
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Admin, Librarian, and Member views
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

    # Add, Edit, Delete Books (permission-based views)
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
