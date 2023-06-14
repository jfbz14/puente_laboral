from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView, View, FormView
from django.urls import reverse_lazy
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

# local
from .forms import PostForm, DataBetaForm
from .models import Posts


class Home(TemplateView):
    """Return home page"""

    template_name = 'home.html'

    def dispatch(self, request,*args, **kwargs):
        """ user started, redirect to start """

        if request.user.is_authenticated:
            return redirect('post:list_booking_wait_gestion')
            
        return super().dispatch(request, *args, **kwargs)
    

class About(TemplateView):
    """Return about page"""

    template_name = 'about.html'


class ListPosts(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/home_login_posts.html'
    model = Posts
    ordering = ('-created',)
    context_object_name = 'posts'


class CreatePostsView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/create_posts.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:home_login_posts')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profileuser
        return context


class ContactView(View):
    """view to send form mail"""
           
    def get(self, request, *args, **kwargs):
        
        return render (request, 'contact.html', context={})

    def post(self, request, *args, **kwargs):

        full_name = self.request.POST['full_name']
        email = self.request.POST['email']
        number = self.request.POST['number']
        subject = self.request.POST['subject']
        content = self.request.POST['content']

        if full_name and email and number and object and content :

            from_email = settings.EMAIL_HOST_USER
            text_content = "This is an important message."
            html_content = "<p>Nombre: {} <br> Asunto: {} <br> Telefono: {} <br>Email:<strong> {} </strong><br> Mensaje:<br> {}.</p>".format(full_name, subject, number, email, content)
            msg = EmailMultiAlternatives('Contac WEb Guiatec {}'.format(full_name), text_content, from_email, [from_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return render (request, 'contact.html', context={'form_valid':True})
        
        return render (request, 'contact.html', context={})
    

class RegisterBetaView(FormView):
    """User signup view."""

    template_name = 'users/data_beta.html'
    form_class = DataBetaForm

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)   

    def get_success_url(self):
        url = "%s?register=register_valid" % reverse('posts:register')
        return url 