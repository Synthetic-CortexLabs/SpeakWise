"""Base models for the SpeakWise application."""

from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating 'created' and 'modified' fields.
    """

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        """Metadata options for the model."""

        abstract = True


class SocialLink(TimestampedModel):
    """Abstract base model for storing social media links."""

    social_name = models.CharField(max_length=50)
    social_url = models.URLField()
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    # Add common methods/validation here
    class Meta:
        abstract = True
        ordering = ["display_order"]

    def __str__(self) -> str:
        if self.social_name:
            return self.social_name
        return "Social Handle Name"
