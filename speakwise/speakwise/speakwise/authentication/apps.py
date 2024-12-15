"""authentication app configuration"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthenticationConfig(AppConfig):
    """Authentication app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
    verbose_name = _("Authentication")
