import os
import random

from django.db import models

# Create your models here.
from django.utils import timezone

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 5345564659)
    name, ext = get_filename_ext(filename)
    final_filename= '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)

class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price       = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    created     = models.DateTimeField(default=timezone.now)
    modified    = models.DateTimeField(null=True, blank=True)
    user_create = models.IntegerField(null=True)
    user_modify = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
