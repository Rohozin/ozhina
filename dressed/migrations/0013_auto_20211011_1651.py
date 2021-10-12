# Generated by Django 3.2.6 on 2021-10-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressed', '0012_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='arm_girth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват руки (плеча)', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='back_width',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='ширина спинки', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='center_chest',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='центр груди', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='chest_girth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват груди', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='chest_height',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='высота груди', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_height',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='полный рост', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hip_girth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват бедер', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='knee_girth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват колена', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='length_front_waist',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='длинна переда до талии', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='long_back_waist',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='длинна спины к талии', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='long_sleeves',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='длинна рукава', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='long_waist_knee',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='длинна от талии до колена', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neck_girth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват шеи', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shoulder_long',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='длина плеча', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='thigh_girth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват бедра', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='waist_circumference',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват талии', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wrist_girth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='обхват кисти', max_digits=10, null=True),
        ),
    ]
