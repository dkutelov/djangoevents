# Generated by Django 3.1.3 on 2020-11-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20201128_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue_address',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
