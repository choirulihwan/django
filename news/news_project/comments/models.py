from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from articles.models import Article


class Comment(models.Model):
    user_comment = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='commentator')
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)
    content = models.TextField(default='')
    input_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content