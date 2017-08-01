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
    image_width = models.CharField(max_length=10)
    image_height = models.CharField(max_length=10)
    image_rotation = models.BooleanField(default=False)

