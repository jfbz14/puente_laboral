"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profileuser
                if not profile.picture or not profile.biography or not profile.document_number or not profile.phone_number or not profile.address or not profile.website or not profile.biography:
                    if request.path not in [reverse('users:update_user'), reverse('users:logout')]:
                        return redirect('users:update_user')

        response = self.get_response(request)
        return response

