# Generated by Django 3.2.6 on 2021-11-25 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0036_formteach'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formteach',
            old_name='cat',
            new_name='course',
        ),
    ]
