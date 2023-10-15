from django.db import models
import os
from django.conf import settings


def content_file_name(instance, filename):
    filename = "input.html"
    return os.path.join(settings.MEDIA_ROOT, filename)

class UploadFile(models.Model):
    file = models.FileField(upload_to=content_file_name)
    title = models.CharField(max_length=50, null = True)

    def __str__(self):
        return "input"