# Generated by Django 3.2.6 on 2021-10-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0018_auto_20211019_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Ім`я'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Контактний номер'),
        ),
    ]