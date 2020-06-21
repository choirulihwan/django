# Generated by Django 3.0.7 on 2020-06-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('0', 'DRAFT'), ('1', 'PUBLISHED')], default='0', max_length=1),
        ),
    ]
