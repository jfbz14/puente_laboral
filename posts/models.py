from django.db import models
from profile_user.models import User, ProfileUser


class Posts(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    description = models.TextField(max_length=500, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)