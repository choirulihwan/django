from django.db import models
from django.utils import timezone


class Note(models.Model):
    title   = models.CharField(null=True, max_length=150)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
