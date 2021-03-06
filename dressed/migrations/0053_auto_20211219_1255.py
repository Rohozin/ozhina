# Generated by Django 3.2.6 on 2021-12-19 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0052_auto_20211213_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecollection',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagecollection',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='collectionuser',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='data/user/documents_collection/'),
        ),
    ]
