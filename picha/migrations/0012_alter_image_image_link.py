# Generated by Django 4.0.3 on 2022-03-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picha', '0011_image_category_image_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_link',
            field=models.ImageField(default=1, upload_to='images/'),
        ),
    ]
