# Generated by Django 3.2.6 on 2021-11-25 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0035_course_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formteach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='Phone number')),
                ('massege', models.TextField(blank=True, max_length=500, null=True, verbose_name='Your wishes')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dressed.course', verbose_name='You')),
            ],
        ),
    ]
