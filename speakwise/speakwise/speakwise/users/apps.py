"""Users app config module."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """Users app config module."""

    name = "speakwise.users"
    verbose_name = _("Users")
