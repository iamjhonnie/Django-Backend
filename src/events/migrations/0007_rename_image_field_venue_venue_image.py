# Generated by Django 4.2.1 on 2023-06-19 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_venue_image_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='image_field',
            new_name='venue_image',
        ),
    ]
