# Generated by Django 5.1.2 on 2024-10-28 11:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="event",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="event",
            name="create_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="event",
            name="update_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
