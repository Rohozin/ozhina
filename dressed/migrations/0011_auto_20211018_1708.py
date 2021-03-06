# Generated by Django 3.2.6 on 2021-10-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0010_rename_url_product_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='imagecollection',
        ),
        migrations.AddField(
            model_name='product',
            name='format_file',
            field=models.TextField(blank=True, max_length=5, verbose_name='Формат електронного документу'),
        ),
        migrations.AddField(
            model_name='product',
            name='money',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Ціна за модель'),
        ),
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.TextField(blank=True, max_length=3, verbose_name='Години консультацій за 1 модель'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
