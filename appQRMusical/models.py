from django.db import models
from django.utils import timezone
import os
# Create your models here.

class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=100)
    resolution = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.id


class Settings(models.Model):
    id = models.AutoField(primary_key=True)
    image_width = models.IntegerField(default=800)
    image_height = models.IntegerField(default=640)
    image_rotation = models.BooleanField(default=False)
    timeout = models.IntegerField(default=5000)


def directory_to_upload(self, file):
    name, extension = os.path.splitext(file)
    directory = ''

    if extension == '.jpg':
        directory = 'images/'

    elif extension == '.mp3':
        directory = 'songs/'

    elif extension == '.ogg':
        directory = 'sounds'

    return os.path.join(directory, file)


class File(models.Model):
    FILE_TYPES = (
        ('mp3', 'Song'),
        ('ogg', 'Sound'),
        ('jpg', 'Image'),
    )
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=directory_to_upload)
    filename = models.CharField(max_length=128, blank=True, null=True)
    filetype = models.CharField(max_length=3, choices=FILE_TYPES, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.filename
