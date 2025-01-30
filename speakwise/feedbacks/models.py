"""feedback models."""

from datetime import timedelta

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from speakwise.attendees.models import Attendee
from speakwise.base.models import TimestampedModel
from speakwise.events.models import Session


class Feedback(TimestampedModel):
    """Feedback model."""

    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=False)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, null=False)
    overall_rating = models.IntegerField(null=False)
    engagement = models.IntegerField(null=False)
    clarity = models.IntegerField(null=False)
    content_depth = models.IntegerField(null=False)
    speaker_knowledge = models.IntegerField(null=False)
    practical_relevance = models.IntegerField(null=False)
    comment = models.TextField(blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)
    is_editable = models.BooleanField(default=True)

    def __str__(self):
        """Return string representation."""
        return f"{self.session} - {self.attendee}"


@receiver(post_save, sender=Feedback)
def update_editable_status(sender, instance, **kwargs):
    """make editable status false after 24 hours of feedback submission."""

    while instance.created_at + timedelta(days=1) < timezone.now():
        instance.is_editable = False
        instance.save()
        break
