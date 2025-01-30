"""Talks app configuration."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TalksConfig(AppConfig):
    """Talks app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "speakwise.talks"
    verbose_name = _("Talks")
