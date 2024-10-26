"""base models for created recurring models that can be inherited by other model to avoid duplications"""

from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    """Timestamped model."""

    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta class."""

        abstract = True
