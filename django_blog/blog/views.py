from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Post

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

    # Restrict access to the post author only
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Post Delete View (Requires login and author restriction)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    # Restrict access to the post author only
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

