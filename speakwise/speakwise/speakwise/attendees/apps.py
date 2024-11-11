"""Attendees app config module."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AttendeesConfig(AppConfig):
    """attendees app config."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'speakwise.attendees'
    verbose_name = _("Attendees")