# Generated by Django 3.2.6 on 2021-10-19 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0014_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='profile',
        ),
    ]