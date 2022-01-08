from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    olx_id = models.CharField(max_length=50, blank=True)
    shopee_id = models.CharField(max_length=50, blank=True)
    tokopedia_id = models.CharField(max_length=50, blank=True)
    instagram_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name