# Generated by Django 3.2.6 on 2021-11-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0022_auto_20211104_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_published',
            field=models.BooleanField(null=True),
        ),
    ]
