# Generated by Django 3.2.6 on 2021-11-20 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0028_imagecollection_clothesmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecollection',
            name='clothesmodel',
        ),
    ]