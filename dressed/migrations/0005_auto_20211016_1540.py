# Generated by Django 3.2.6 on 2021-10-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0004_auto_20211014_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='format_file',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='time',
        ),
        migrations.AddField(
            model_name='imagecollection',
            name='format_file',
            field=models.TextField(blank=True, max_length=5, verbose_name='Формат електронного документу'),
        ),
        migrations.AddField(
            model_name='imagecollection',
            name='time',
            field=models.TextField(blank=True, max_length=3, verbose_name='Години консультацій за 1 модель'),
        ),
    ]
