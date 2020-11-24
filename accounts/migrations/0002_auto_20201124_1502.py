# Generated by Django 3.1.3 on 2020-11-24 15:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photoURL',
        ),
        migrations.AddField(
            model_name='profile',
            name='userPhotoURL',
            field=cloudinary.models.CloudinaryField(default='null', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]