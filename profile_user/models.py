from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class User (AbstractUser):
    """Model User"""

    email = models.EmailField(_('email'), blank=True, unique=True)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/profile/{1}'.format(instance.user.id, filename)


class ProfileUser(models.Model):
    """Model Profile_User"""

    DOCUMENT_TYPE_CHOICES = [
        ('cc', _('identification document')),
        ('ce', _('foreigner id')),
        ('pa', _('passsport')),
    ]  
    
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.PROTECT)
    document_type = models.CharField(_('document type'), max_length=50, choices=DOCUMENT_TYPE_CHOICES, default='cc')
    document_number = models.CharField(_('document number'), max_length=50)
    picture = models.ImageField(_('image profile'), upload_to=user_directory_path)
    phone_number = PhoneNumberField(_('phone number'), unique=True)
    address = models.CharField(_('address'), max_length=50)
    website = models.CharField(_('website'), max_length=200)
    biography = models.TextField(_('biography'), max_length=150)
    validated = models.BooleanField(_('validated'),default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """ return firts_name and last_name """

        return self.user.get_full_name()
    

class ServiceCategory(models.Model):
    """ model servicecategory """

    name = models.CharField(_('name category'), max_length=50, unique=True)
    

class ServiceProfile(models.Model):
    """Model service profile"""

    name_category = models.ForeignKey(ServiceCategory, verbose_name=_('name category'), on_delete=models.CASCADE)
    title_servicie = models.CharField(_('title service'), max_length=50)
    description = models.TextField(_('description'), max_length=255)
    price = models.CharField(_('price'), max_length=150)
    

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