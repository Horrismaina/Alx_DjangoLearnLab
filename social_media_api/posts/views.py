from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from rest_framework.decorators import action
from notifications.models import Notification 
from notifications.serializers import NotificationSerializer  # <-- Import the serializer


# Post view set for handling CRUD operations for posts
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
        post = self.get_object()
        user = request.user
        if Like.objects.filter(post=post, user=user).exists():
            return Response({'detail': 'You have already liked this post.'}, status=400)
        Like.objects.create(post=post, user=user)
        return Response({'detail': 'Post liked.'}, status=201)

    # Unlike a post (Custom action)
    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like = Like.objects.filter(post=post, user=user)
        if not like.exists():
            return Response({'detail': 'You have not liked this post.'}, status=400)
        like.delete()
        return Response({'detail': 'Post unliked.'}, status=200)

# Comment view set for handling CRUD operations for comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Feed view for displaying posts from followed users
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Assuming `following` is a ManyToManyField in CustomUser
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

# Notification view for fetching user's notifications (this view can be expanded later)
class NotificationView(generics.ListAPIView):
    # Assuming a Notification model exists that records notifications for users
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

