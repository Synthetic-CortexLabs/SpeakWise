# Generated by Django 5.0.9 on 2024-11-08 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]