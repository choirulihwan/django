# Generated by Django 3.0.7 on 2020-06-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referensi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ref', models.CharField(max_length=3)),
                ('no_ref', models.CharField(max_length=20)),
                ('keterangan', models.CharField(max_length=150)),
                ('keterangan_label', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]