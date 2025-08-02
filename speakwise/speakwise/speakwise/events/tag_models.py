"""Models for event tagging in the SpeakWise application."""

from django.db import models
from speakwise.base.models import TimestampedModel


class Tag(TimestampedModel):
    """A model for event tags in the SpeakWise application."""

    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=20, default="#007bff")

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


"""
Add this to events/models.py:

from .tag_models import Tag

# In the Event model:
tags = models.ManyToManyField(Tag, related_name="events", blank=True)
"""
