# Generated by Django 3.2.6 on 2021-10-19 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dressed', '0017_auto_20211019_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, upload_to='order/', verbose_name='Завантажте зображення'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]