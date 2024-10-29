"""This module contains the SpeakersConfig class that inherits from AppConfig."""

from django.apps import AppConfig


class SpeakersConfig(AppConfig):
    """Speakers configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "speakers"
