# Generated by Django 3.0.7 on 2020-06-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='groups',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
