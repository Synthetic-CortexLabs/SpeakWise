# Generated by Django 5.0.9 on 2024-10-30 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_end_at_alter_event_start_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_at',
            new_name='end_date_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_at',
            new_name='start_date_time',
        ),
    ]
