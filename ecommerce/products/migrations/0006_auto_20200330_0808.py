# Generated by Django 3.0.4 on 2020-03-30 01:08

from django.db import migrations, models
import django.utils.timezone
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200330_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]
