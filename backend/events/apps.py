"""This module contains the configuration for the events app."""

from django.apps import AppConfig


class EventsConfig(AppConfig):
    """Events configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "events"
