import os
import random

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse

from products.utils import unique_slug_generator

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

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = Q(title__icontains=query) | \
                  Q(description__icontains=query) | \
                  Q(price__icontains=query)
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
         return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Product(models.Model):
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField(null=True)
    price       = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    created     = models.DateTimeField(default=timezone.now)
    modified    = models.DateTimeField(null=True, blank=True)
    user_create = models.IntegerField(null=True)
    user_modify = models.IntegerField(null=True, blank=True)

    objects = ProductManager()

    def get_absolute_url(self):
        # return '/products/{slug}'.format(slug=self.slug)
        return reverse('products:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)