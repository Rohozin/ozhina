# Generated by Django 3.2.6 on 2021-10-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0016_remove_order_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='massege',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Доповнення'),
        ),
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, upload_to='order/', verbose_name='Завантажте зображення яке'),
        ),
    ]