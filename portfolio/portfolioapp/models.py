from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField 
from distutils.command import upload

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)