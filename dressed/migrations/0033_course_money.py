# Generated by Django 3.2.6 on 2021-11-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0032_imagecollection_clothesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='money',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price for 1 lessons'),
        ),
    ]