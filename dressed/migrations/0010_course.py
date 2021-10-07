# Generated by Django 3.2.6 on 2021-10-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0009_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('about', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='course')),
                ('lessons_circle', models.DecimalField(decimal_places=2, max_digits=10)),
                ('circle', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.TextField(max_length=51)),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ('name',),
            },
        ),
    ]