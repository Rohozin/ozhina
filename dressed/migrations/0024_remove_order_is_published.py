# Generated by Django 3.2.6 on 2021-11-06 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0023_order_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_published',
        ),
    ]
