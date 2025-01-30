"""Organizers app configuration."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrganizersConfig(AppConfig):
    """Organizers app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "speakwise.organizers"
    verbose_name = _("Organizers")
