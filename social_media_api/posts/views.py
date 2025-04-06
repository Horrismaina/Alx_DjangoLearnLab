from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404  # Importing get_object_or_404 correctly
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from accounts.models import CustomUser
from notifications.models import Notification  # Ensure you import the Notification model
from notifications.serializers import NotificationSerializer  # Ensure you import the NotificationSerializer
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Like a post (Custom action)
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Correctly fetch the Post object
        user = request.user
        
        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(post=post, user=user)  # Use get_or_create
        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=400)
        
        # Create a notification for the post's author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )
        
        return Response({'detail': 'Post liked.'}, status=201)

    # Unlike a post (Custom action)
    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Correctly fetch the Post object
        user = request.user
        
        like = Like.objects.filter(post=post, user=user)
        if not like.exists():
            return Response({'detail': 'You have not liked this post.'}, status=400)
        
        like.delete()  # Delete the like
        
        # Optionally, you could create a notification for unliking as well
        return Response({'detail': 'Post unliked.'}, status=200)

# Notification view for fetching user's notifications
class NotificationView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
