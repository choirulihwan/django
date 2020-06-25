from django.db import models
from django.db.models.signals import pre_save

from news_project.utils import unique_slug_generator

# Create your models here.
class Category(models.Model):
    cat_name    = models.CharField(max_length=50)
    slug        = models.SlugField(blank=True)

    def __str__(self):
        return self.cat_name

def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.title = instance.cat_name
        instance.slug = unique_slug_generator(instance)

pre_save.connect(category_pre_save_receiver, sender=Category)