"""speakers app configuration."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SpeakersConfig(AppConfig):
    """Speakers app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "speakwise.speakers"
    verbose_name = _("Speakers")
