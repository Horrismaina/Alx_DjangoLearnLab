from django.urls import path
from .views import post_detail, comment_edit, comment_delete

urlpatterns = [
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/<int:post_id>/comment/<int:comment_id>/edit/', comment_edit, name='comment-edit'),
    path('post/<int:post_id>/comment/<int:comment_id>/delete/', comment_delete, name='comment-delete'),
]
