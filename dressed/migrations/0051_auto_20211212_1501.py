# Generated by Django 3.2.6 on 2021-12-12 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0050_remove_imagecollection_clothesmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecollection',
            name='format_file',
        ),
        migrations.RemoveField(
            model_name='imagecollection',
            name='time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='money',
        ),
    ]
