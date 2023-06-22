from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import validate_email


class User (AbstractUser):
    """Model User"""

    email = models.EmailField("Correo electrónico", blank=True, unique=True)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/profile/{1}'.format(instance.user.id, filename)


class ProfileUser(models.Model):
    """Model Profile_User"""

    DOCUMENT_TYPE_CHOICES = [
        ('CC', 'CEDULA DE CIUDADANIA'),
        ('CE', 'CEDULA DE EXTRANJERIA'),
        ('PA', 'PASAPORTE'),
        ('TI', 'TARJETA DE IDENTIDAD'),
        ('IT', 'IDENTIFICACION TRIBUTARIA'),
        ('IP', 'IDENTIFICACION PERSONAL'),
    ]  
    
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    document_type = models.CharField(verbose_name='Tipo de Documento', max_length=50, choices=DOCUMENT_TYPE_CHOICES, default='CC')
    document_number = models.CharField(verbose_name='Numero de Documento', max_length=50)
    picture = models.ImageField(verbose_name='Imagen de Perfil', upload_to=user_directory_path)
    phone_number = models.CharField(verbose_name='Numero de Telefono', max_length=10)
    address = models.CharField(verbose_name='Dirección', max_length=50)
    website = models.CharField(verbose_name='Link', max_length=200)
    biography = models.TextField(verbose_name='Descripción', max_length=150)
    validated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """ return firts_name and last_name """

        return self.user.get_full_name()
    

class ModelDataBeta(models.Model):
    """ model data beta """   

    DOCUMENT_TYPE_CHOICES = [
        ('CC', 'CEDULA DE CIUDADANIA'),
        ('CE', 'CEDULA DE EXTRANJERIA'),
        ('PA', 'PASAPORTE'),
        ('IP', 'IDENTIFICACION PERSONAL'),
    ] 

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_type = models.CharField(max_length=3, choices=DOCUMENT_TYPE_CHOICES, default='CC')
    document_number = models.CharField(max_length=50, unique=True, error_messages={
            "unique": "Documento está registrado",
        },)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    occupation = models.TextField(max_length=250)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        """return last_name and doucemnt_number"""

        return '{} - {}'.format(self.first_name, self.document_number)
    
    def save(self, *args, **kwargs ):
        """for uppercase fields"""

        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        self.email = self.email.upper()
        self.city = self.city.upper()
        self.address = self.address.upper()
        self.neighborhood = self.neighborhood.upper()
        self.occupation = self.occupation.upper()

        super().save(*args, **kwargs)