# Generated by Django 3.2.6 on 2021-11-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0031_remove_imagecollection_clothesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecollection',
            name='clothesmodel',
            field=models.FileField(blank=True, null=True, upload_to='clothesmodel/', verbose_name='clothesmodel'),
        ),
    ]