from django.db import models

from speakwise.base.models import TimestampedModel
from speakwise.events.models import Event


class Attendee(TimestampedModel):
    """Attendee model."""

    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    notification_preference = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    is_verified = models.BooleanField(default=False)


class AttendanceCode(TimestampedModel):
    """Attendee code model."""

    code = models.CharField(max_length=255, null=True)
    attendee = models.OneToOneField(
        Attendee,
        null=True,
        on_delete=models.CASCADE,
        related_name="attendee_unique_code",
    )
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, null=True)
    is_used = models.BooleanField(default=False)
