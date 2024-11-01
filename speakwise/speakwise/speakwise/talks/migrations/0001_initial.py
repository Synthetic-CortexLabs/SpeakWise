# Generated by Django 5.0.9 on 2024-11-01 17:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("events", "0007_session"),
        ("speakers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Talks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "event_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="events.event",
                    ),
                ),
                ("speaker_id", models.ManyToManyField(to="speakers.speaker")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
