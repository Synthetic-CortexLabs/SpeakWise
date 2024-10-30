"""Base models for the SpeakWise application."""

from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    """An abstract base class model that provides self-updating 'created' and 'modified' fields."""

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(timezone.now)

    class Meta:
        """Metadata options for the model."""

        abstract = True
