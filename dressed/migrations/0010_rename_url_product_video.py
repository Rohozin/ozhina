# Generated by Django 3.2.6 on 2021-10-17 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0009_product_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='url',
            new_name='video',
        ),
    ]
