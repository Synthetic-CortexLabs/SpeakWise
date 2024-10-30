from base.models import TimestampedModel
from django.db import models
from django.utils import timezone


class Event(TimestampedModel):
    """A model for events in the SpeakWise application."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date_time = models.DateTimeField(default=timezone.now)
    end_date_time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
