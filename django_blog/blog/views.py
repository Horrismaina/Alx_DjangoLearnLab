from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Import Q for complex query lookups
from django.shortcuts import render
from .models import Post, Comment  # Import Comment model
from django.views.generic import ListView
from taggit.models import Tag  # Import the Tag model from django-taggit


# Post List View (No login required)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Post Detail View (No login required)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Post Create View (Requires login)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

# Post Update View (Requires login and author restriction)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author remains the same
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Post Delete View (Requires login and author restriction)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# --- Comment Views ---

# Comment Create View (Requires login)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])  # Get the related post
        form.instance.author = self.request.user  # Set the author to the logged-in user
        form.instance.post = post  # Attach the comment to the correct post
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the post detail page


# Comment Update View (Requires login and author restriction)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author remains the same
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only allow the comment's author to update

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the post detail page


# Comment Delete View (Requires login and author restriction)
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only allow the comment's author to delete

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the post detail page after deletion

def PostSearchView(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |  # Search by title
            Q(content__icontains=query) |  # Search by content
            Q(tags__name__icontains=query)  # Search by tags
        ).distinct()
    else:
        results = Post.objects.none()  # No results if no query

    context = {
        'posts': results,
        'query': query
    }
    return render(request, 'blog/post_search.html', context)

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Get the tag name from the URL
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return Post.objects.filter(tags=tag)  # Filter posts by the tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('slug'))  # Add the tag to the context
        return context