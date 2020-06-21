from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from tinymce.models import HTMLField

from categories.models import Category
from news_project.utils import unique_slug_generator

STATUS_CHOICES = [
    ('0', 'DRAFT'),
    ('1', 'PUBLISHED'),
]
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    content = models.TextField(default='')
    # content = HTMLField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    user_input = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='writer')
    user_update = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='editor')
    input_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(article_pre_save_receiver, sender=Article)