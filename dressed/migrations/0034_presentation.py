# Generated by Django 3.2.6 on 2021-11-21 19:18

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0033_course_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('about', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
    ]