from django.db import models

# Create your models here.
class Referensi(models.Model):
    id_ref  = models.CharField(max_length=3)
    no_ref  = models.CharField(max_length=20)
    keterangan  = models.CharField(max_length=150)
    keterangan_label = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.keterangan
