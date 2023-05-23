from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy

# local
from .forms import PostForm
from .models import Post


class Home(TemplateView):
    """Return home page"""

    template_name = 'home.html'


class ListPosts(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/index.html'
    model = Post
    ordering = ('-created',)
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('post:index')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profileuser
        return context

    