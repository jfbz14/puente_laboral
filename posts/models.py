from django.db import models
from django.core.validators import FileExtensionValidator
from pathlib import Path            
from profile_user.models import User, ProfileUser
from django.utils.translation import gettext_lazy as _

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/posts/{1}'.format(instance.user.id, filename)


class Posts(models.Model):
    """Post model."""
    
    EXT_FILE_VIDEO = ['MOV','avi','mp4','webm','mkv','f4v']
    EXT_FILE_IMAGE = ['jpg','git']
    EXT_FILE_VALID = EXT_FILE_VIDEO + EXT_FILE_IMAGE

    CHOICE_TYPE_MEDIA =[
        ('image', 'image'),
        ('video', 'video'),
    ]
    user = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.CASCADE, related_name=_('posts'))
    title = models.CharField(_('title'), max_length=75)
    media_file = models.FileField(_("media file"), upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=EXT_FILE_VALID)], null=True, blank=True)
    type_media = models.CharField(_('type media'), max_length=15,choices=CHOICE_TYPE_MEDIA, default='video')
    description = models.TextField(_("description"), max_length=300, blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)
    
    def save(self, *args, **kwargs ):
        """
            Valida extension del archivo, para guardar su tipo
            Validate file extension, to save its type        """

        get_ext=Path(self.media_file.name).suffix.replace('.','')
        if get_ext in self.EXT_FILE_VIDEO:
            self.type_media = 'video'  
        elif get_ext in self.EXT_FILE_IMAGE:
            self.type_media = 'image'

        super().save(*args, **kwargs)