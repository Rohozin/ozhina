# Generated by Django 3.2.6 on 2021-12-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0042_auto_20211205_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectionuser',
            name='profile',
        ),
        migrations.AddField(
            model_name='collectionuser',
            name='clothingparameters',
            field=models.TextField(help_text='parameters: pg96,gk107', null=True),
        ),
    ]