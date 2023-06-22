# Django
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView, TemplateView, DetailView
from django.urls import reverse_lazy, reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.views import PasswordChangeView

# local
from .forms import UpdateFormProfileUser, CreateSigupForm
from .models import ProfileUser, User
from posts.models import Posts


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'

    def dispatch(self, request,*args, **kwargs):
        """ user started, redirect to start """

        if request.user.is_authenticated:
            return redirect('posts:index')
            
        return super().dispatch(request, *args, **kwargs)
    

class SignupView(FormView):
    """User signup view."""

    template_name = 'users/signup.html'
    form_class = CreateSigupForm
    success_url = reverse_lazy('users:login')

    def dispatch(self, request,*args, **kwargs):
        """ user started, redirect to start """

        if request.user.is_authenticated:
            return redirect('post:index')
            
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
    

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html' 


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """profile update"""

    template_name = 'users/update_user.html'
    form_class = UpdateFormProfileUser
    model = ProfileUser

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profileuser
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""

        firts_name = self.request.POST['first_name']
        last_name = self.request.POST['last_name']
        username = self.request.POST['username']
        email = self.request.POST['email']

        try:
            #Check if it is email.
            validate_email(email)
        except ValidationError:
            self.extra_context = {'email_errors': 'Correo ({}) invalido.'.format(email)}
            return super().form_invalid(form)
                
        if firts_name and last_name and email and username:
            id = self.object.user.id
            user = get_object_or_404(User, id=id)

            valid_email = User.objects.filter(email=email).exclude(id=user.pk).exists()
            if valid_email == True:
                """Email or username must be unique."""
                self.extra_context = {'email_errors': 'El correo ({}) ya se encuentra en uso.'.format(email)}
                return super().form_invalid(form) 
            
            valid_username = User.objects.filter(username=username).exclude(id=user.pk).exists()
            if valid_username == True:
                """Email or username must be unique."""
                self.extra_context = {'username_errors': 'El usuario ({}) ya se encuentra en uso.'.format(username)}
                return super().form_invalid(form) 

            user.username = username
            user.first_name = firts_name
            user.last_name = last_name
            user.email = email
            user.save()
            form.save()
            return super().form_valid(form)
        return super().form_invalid(form)
    
    def get_success_url(self):
        url = "%s?update=valid" % reverse('users:update_user')
        return url
    

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """ Change password"""

    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:index')
 

class ListDashboarUser(LoginRequiredMixin, DetailView):

    """Return post detail."""

    template_name = 'users/dashboard_user.html'
    queryset =User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Posts.objects.all().filter(user=self.object)
        return context
    