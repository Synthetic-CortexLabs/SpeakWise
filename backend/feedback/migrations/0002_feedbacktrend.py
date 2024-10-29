# Generated by Django 5.1.2 on 2024-10-29 22:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0001_initial"),
        ("talks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedbackTrend",
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
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("date", models.DateField()),
                ("average_daily_rating", models.FloatField()),
                ("daily_feedback_count", models.PositiveIntegerField()),
                ("positive_feedback_count", models.PositiveIntegerField()),
                (
                    "talk_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trends",
                        to="talks.talks",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
