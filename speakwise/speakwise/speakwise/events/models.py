"""Models for the events app in the SpeakWise application."""

from base.models import TimestampedModel
from django.db import models
from django.utils import timezone


class Event(TimestampedModel):
    """A model for events in the SpeakWise application."""

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=255, null=True)
    start_date_time = models.DateTimeField(default=timezone.now, null=True)
    end_date_time = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=False, null=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title


class Country(TimestampedModel):
    """A model for countries in the SpeakWise application."""

    name = models.CharField(max_length=255, null=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="country",
    )

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Region(TimestampedModel):
    """A model for regions in the SpeakWise application."""

    name = models.CharField(max_length=255, null=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="region",
    )

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Session(TimestampedModel):
    """A model for sessions in the SpeakWise application."""

    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    start_date_time = models.DateTimeField(default=timezone.now, null=True)
    end_date_time = models.DateTimeField(default=timezone.now, null=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="session",
    )
    location = models.CharField(max_length=255, null=True)

    # TODO: Add speaker field
    speaker = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
