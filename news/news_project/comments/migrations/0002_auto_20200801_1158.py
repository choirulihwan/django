# Generated by Django 3.0.8 on 2020-08-01 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200621_1449'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.Article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commentator', to=settings.AUTH_USER_MODEL),
        ),
    ]
