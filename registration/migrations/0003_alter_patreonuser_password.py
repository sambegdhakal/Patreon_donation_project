# Generated by Django 5.0.3 on 2024-04-01 00:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "registration",
            "0002_alter_patreonuser_options_alter_patreonuser_managers_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="patreonuser",
            name="password",
            field=models.CharField(max_length=128),
        ),
    ]
