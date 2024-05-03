# Generated by Django 5.0.3 on 2024-05-03 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_image_image_file'),
        ('page', '0014_alter_patreonpage_banner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patreonpage',
            name='subscriber_count',
        ),
        migrations.AlterField(
            model_name='patreonpage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='images.image'),
        ),
    ]
