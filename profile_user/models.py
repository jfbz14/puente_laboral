from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    email = models.EmailField(blank=True, unique=True)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class ProfileUser (models.Model):

    DOCUMENT_TYPE_CHOICES = [
        ('CC', 'CEDULA DE CIUDADANIA'),
        ('CE', 'CEDULA DE EXTRANJERIA'),
        ('PA', 'PASAPORTE'),
        ('TI', 'TARJETA DE IDENTIDAD'),
        ('IT', 'IDENTIFICACION TRIBUTARIA'),
        ('IP', 'IDENTIFICACION PERSONAL'),
    ]  
    
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES, default='CC', blank=True)
    document_number = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    validated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """ return firts_name and last_name """

        return self.user.get_full_name()
  