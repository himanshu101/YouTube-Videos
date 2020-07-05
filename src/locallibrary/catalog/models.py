import jsonfield

from django.db import models
from django_mysql.models import EnumField
from django.utils import timezone

from .constants.app_constants import AppConstants

# Create your models here.


class Video(models.Model):
    title = models.TextField()
    description = models.TextField(null=False)
    thumbnails = jsonfield.JSONField(help_text='Storing thumbnails for videos', default=dict)
    source = EnumField(choices=[AppConstants.VIDEO_SOURCE_YOUTUBE], default=AppConstants.VIDEO_SOURCE_YOUTUBE, db_index=True)
    video_id = models.CharField(max_length=200, null=True)
    published_at = models.DateTimeField(null=False, default=timezone.now())
    created_at = models.DateTimeField(auto_now=True)
