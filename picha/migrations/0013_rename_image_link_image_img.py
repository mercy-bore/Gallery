# Generated by Django 4.0.3 on 2022-03-26 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picha', '0012_alter_image_image_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_link',
            new_name='img',
        ),
    ]
