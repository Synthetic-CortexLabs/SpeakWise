# Generated by Django 5.1.2 on 2024-10-29 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_created_at_remove_event_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]