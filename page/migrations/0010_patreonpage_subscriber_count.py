# Generated by Django 5.0.3 on 2024-04-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("page", "0009_remove_patreonpage_goal_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="patreonpage",
            name="subscriber_count",
            field=models.IntegerField(default=0),
        ),
    ]
