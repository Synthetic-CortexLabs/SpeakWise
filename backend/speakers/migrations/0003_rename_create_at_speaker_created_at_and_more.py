# Generated by Django 5.1.2 on 2024-10-28 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_remove_speaker_created_at_remove_speaker_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='speaker',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
