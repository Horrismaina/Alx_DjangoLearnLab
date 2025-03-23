from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostSearchView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    search
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', search, name='search'),
    path('search/', PostSearchView, name='post-search'),
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),
    
    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Update existing comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete existing comment
]
