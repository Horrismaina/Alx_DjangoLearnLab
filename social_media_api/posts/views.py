from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404  # Importing the correct get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from accounts.models import CustomUser
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
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

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Correct way to get Post by pk
        user = request.user
        
        # Like or create a Like object
        like, created = Like.objects.get_or_create(user=user, post=post)
        
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

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Correct way to get Post by pk
        user = request.user
        
        # Get and delete the like object if exists
        like = Like.objects.filter(user=user, post=post)
        if not like.exists():
            return Response({'detail': 'You have not liked this post.'}, status=400)
        
        like.delete()  # Delete the like
        
        return Response({'detail': 'Post unliked.'}, status=200)

class NotificationView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
