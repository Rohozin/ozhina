# Generated by Django 3.2.6 on 2021-10-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0006_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='arm_girth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват руки (плеча)'),
        ),
        migrations.AddField(
            model_name='profile',
            name='back_width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Ширина спинки'),
        ),
        migrations.AddField(
            model_name='profile',
            name='center_chest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Центр грудей'),
        ),
        migrations.AddField(
            model_name='profile',
            name='chest_girth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват грудей'),
        ),
        migrations.AddField(
            model_name='profile',
            name='chest_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Висота грудей'),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Повний зріст'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hair',
            field=models.TextField(blank=True, max_length=100, verbose_name='Колір волосся'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hip_girth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват стегон'),
        ),
        migrations.AddField(
            model_name='profile',
            name='knee_girth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват коліна'),
        ),
        migrations.AddField(
            model_name='profile',
            name='length_front_waist',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Довжина переду до талії'),
        ),
        migrations.AddField(
            model_name='profile',
            name='long_back_waist',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Довжина спини до талії'),
        ),
        migrations.AddField(
            model_name='profile',
            name='long_sleeves',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Довжина рукава'),
        ),
        migrations.AddField(
            model_name='profile',
            name='long_waist_knee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Довжина від талії до коліна'),
        ),
        migrations.AddField(
            model_name='profile',
            name='neck_girth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват шиї'),
        ),
        migrations.AddField(
            model_name='profile',
            name='shoulder_long',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Довжина плеча'),
        ),
        migrations.AddField(
            model_name='profile',
            name='thigh_girth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват стегна'),
        ),
        migrations.AddField(
            model_name='profile',
            name='waist_circumference',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват талії'),
        ),
        migrations.AddField(
            model_name='profile',
            name='wrist_girth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Обхват кисті'),
        ),
    ]
