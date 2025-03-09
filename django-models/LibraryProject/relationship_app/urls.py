from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Root URL path
    path('', views.list_books, name='home'),  # This will serve as the homepage

    # Existing paths
    
    path('books/', views.list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('libraries/', views.LibraryListView.as_view(), name='list_libraries'),  # Class-based view for listing libraries
    path('register/', views.register, name='register'),
    
    # Authentication paths
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
] 
