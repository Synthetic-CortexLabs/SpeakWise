# filepath: /Users/macbook/Desktop/Devs/SpeakWise/speakwise/speakwise/speakwise/events/models.py
"""Models for the events app in the SpeakWise application."""

from speakwise.base.models import TimestampedModel
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models
from django.utils import timezone

EVENT_IMAGE_UPLOAD = "event_images/"


class Tag(TimestampedModel):
    """A model for event tags in the SpeakWise application."""

    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=20, default="#007bff")

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Event(TimestampedModel):
    """A model for events in the SpeakWise application."""

    title = models.CharField(max_length=255, unique=True)
    event_nickname = models.CharField(max_length=255, blank=True, default="")
    event_image = CloudinaryField(
        "image", folder=EVENT_IMAGE_UPLOAD, null=True, blank=True
    )
    short_description = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Brief description for event cards",
    )
    description = models.TextField(
        blank=True, default="", help_text="Detailed description for event page"
    )
    website = models.URLField(max_length=255, blank=True, default="")
    location = models.ForeignKey(
        "Location",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="event_location",
    )
    start_date_time = models.DateTimeField(default=timezone.now, null=True)
    end_date_time = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="events", blank=True)

    # Add organizer relationship
    organizer = models.ForeignKey(
        "organizers.Organizers",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="organized_events",
        help_text="The organizer who created this event",
    )

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    document = models.FileField(
        upload_to="documents/",
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
    )


class Region(TimestampedModel):
    """A model for regions in the SpeakWise application."""

    name = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Regions"

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Location(TimestampedModel):
    """location models for events."""

    venue = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    description = models.TextField(null=True)
    region = models.ForeignKey(
        "Region",
        on_delete=models.CASCADE,
        null=True,
        related_name="location_region",
    )
    country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        null=True,
        related_name="location_country",
    )


class Country(TimestampedModel):
    """A model for countries in the SpeakWise application."""

    name = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Session(TimestampedModel):
    """A model for sessions in the SpeakWise application.

    This model connects events with speakers and includes session-specific details.
    """

    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    start_date_time = models.DateTimeField(default=timezone.now, null=True)
    end_date_time = models.DateTimeField(default=timezone.now, null=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="sessions",
    )
    # location could be a model that contain country
    location = models.ForeignKey(
        "Location",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="session_location",
    )

    # Connect to SpeakerProfile directly
    speaker = models.ForeignKey(
        "speakers.SpeakerProfile",
        on_delete=models.SET_NULL,
        null=True,
        related_name="speaking_sessions",
    )

    def __str__(self):
        return self.name
