# Generated by Django 3.0.4 on 2020-03-29 15:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200329_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 15, 48, 39, 2240, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='user_modify',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
