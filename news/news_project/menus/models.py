from django.contrib.auth.models import Group
from django.db import models

# Create your models here.
class Menu(models.Model):
    name    = models.CharField(max_length=50)
    link    = models.CharField(max_length=50)
    icon    = models.CharField(max_length=30)
    is_active   = models.BooleanField(default=True)
    # parent child
    parent_id   = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    urutan  = models.IntegerField()
    groups  = models.ManyToManyField(Group)

    def __str__(self):
        return self.name


