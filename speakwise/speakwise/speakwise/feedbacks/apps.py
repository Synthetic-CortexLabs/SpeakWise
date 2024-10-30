"""Feedbacks app configuration."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FeedbacksConfig(AppConfig):
    """Feedbacks app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "speakwise.feedbacks"
    verbose_name = _("Feedbacks")
