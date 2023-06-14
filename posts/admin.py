# Django
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Model
from .models import Posts


class PostResource(resources.ModelResource):

    class Meta:
        model = Posts


@admin.register(Posts)
class PostAdmin(ImportExportModelAdmin):
    """Profile admin."""

    resource_class = PostResource
    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user',)

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title',
    )

    list_filter = (
        'created',
        'modified',
    )

    list_per_page = 15
