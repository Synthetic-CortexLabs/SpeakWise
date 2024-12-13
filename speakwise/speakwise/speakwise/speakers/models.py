"""Speakers models."""

from base.models import TimestampedModel
from django.conf import settings
from django.db import models
from django.urls import reverse

# Speakers file upload directory
SPEAKERS_UPLOAD_DIR = "speakers/avatars/"

class Speaker(TimestampedModel):
    """Speaker Model for the SpeakWise application."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="speaker_profile",
    )
    # TODO: ADD EVENT FOREIGN KEY
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
