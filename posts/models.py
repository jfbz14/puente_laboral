from django.db import models
from profile_user.models import User, ProfileUser

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/posts/{1}'.format(instance.user.id, filename)


class Posts(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=75)
    photo = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(max_length=300, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)