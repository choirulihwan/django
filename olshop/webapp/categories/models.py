from django.db import models
from stores.models import Store


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name