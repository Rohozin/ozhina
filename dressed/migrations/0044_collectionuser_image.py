# Generated by Django 3.2.6 on 2021-12-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0043_auto_20211205_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='imgusercollection/'),
        ),
    ]
