from django.db import models
from django.utils import timezone
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

class File(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='images/')
#    file_type = models.
    upload_date = models.DateTimeField(auto_now_add=True)
