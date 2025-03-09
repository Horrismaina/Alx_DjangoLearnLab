from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Root URL path
    path('', views.list_books_html, name='home'),
    
    # Plain text function-based view (for the checker)
    path('books/', views.list_books, name='list_books'),
    
    # HTML version
    path('books-html/', views.list_books_html, name='list_books_html'),
    
    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication paths
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]