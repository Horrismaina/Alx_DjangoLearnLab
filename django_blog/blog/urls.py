from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),          # Display all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Show individual post
    path('post/new/', PostCreateView.as_view(), name='post-create'),       # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]
