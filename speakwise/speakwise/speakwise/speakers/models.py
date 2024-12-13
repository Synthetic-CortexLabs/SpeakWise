"""Speakers models."""

from base.models import TimestampedModel
from django.conf import settings
from django.db import models
from django.urls import reverse

from speakwise.events.models import Event
from speakwise.feedbacks.models import Feedback

# Speakers file upload directory
SPEAKERS_UPLOAD_DIR = "speakers/avatars/"


class Speaker(TimestampedModel):
    """Speaker Model for the SpeakWise application."""

    speaker_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="speaker_profile",
    )
    event = models.ManyToManyField(Event, blank=True, related_name="speakers")
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, null=True)
    organization = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to=SPEAKERS_UPLOAD_DIR, null=True,
                               blank=True)

    class Meta:
        db_table = "speakers"
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("speaker_detail", kwargs={"pk": self.pk})


class Handles(TimestampedModel):
    social_name = models.CharField(max_length=50, null=True)
    social_link = models.URLField(max_length=200, null=True)
    speakers = models.ForeignKey(
        Speaker,
        on_delete=models.DO_NOTHING,
        related_name="speakers_social_accounts",
        null=True,
    )

    class Meta:
        ordering = ["social_name"]
        db_table = "Handles "
        verbose_name = "Handles"
        verbose_name_plural = "Handles"

    def __str__(self) -> str:
        if self.social_name:
            return f"{self.social_name} ({self.social_link})"
        return None  # noqa: PLE0307


