"""Events app configuration."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventsConfig(AppConfig):
    """Events app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "speakwise.events"
    verbose_name = _("Events")
