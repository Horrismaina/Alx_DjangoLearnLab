from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from .models import Post

# Post List View (No login required)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5  # Show 5 posts per page
    ordering = ['-date_posted']  # Order by the newest posts first

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
        messages.success(self.request, 'Your post has been created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})  # Redirect to the post detail after creation

# Post Update View (Requires login and author restriction)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author remains the same
        messages.success(self.request, 'Your post has been updated successfully!')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Restrict access to the post author only

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})  # Redirect to the post detail after update

# Post Delete View (Requires login and author restriction)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'  # Redirect to homepage after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Restrict access to the post author only

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your post has been deleted successfully!')
        return super().delete(request, *args, **kwargs)


