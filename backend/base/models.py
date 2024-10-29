"""base models for created recurring models that can be inherited by other 
model to avoid duplications"""

from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    """Timestamped model."""

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta class."""

        abstract = True
