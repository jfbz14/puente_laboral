# Generated by Django 4.1.7 on 2023-06-30 02:31

import django.core.validators
from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='title')),
                ('media_file', models.FileField(blank=True, null=True, upload_to=posts.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'f4v', 'jpg', 'git'])], verbose_name='media file')),
                ('type_media', models.CharField(choices=[('image', 'image'), ('video', 'video')], default='video', max_length=15, verbose_name='type media')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
        ),
    ]
