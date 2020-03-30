from django.db import models

# Create your models here.
from django.utils import timezone


class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price       = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    created     = models.DateTimeField(default=timezone.now())
    modified    = models.DateTimeField(null=True, blank=True)
    user_create = models.IntegerField(null=True)
    user_modify = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
