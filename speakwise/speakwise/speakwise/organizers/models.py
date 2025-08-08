"""Organizer models."""

import csv
import io
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

from speakwise.base.models import TimestampedModel
from speakwise.events.models import Event
from speakwise.organizers.utils import process_csv_file
from speakwise.users.models import User


class Organizers(TimestampedModel):
    """Organizer model."""

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    events = models.ForeignKey(
        Event,
        verbose_name=("events"),
        on_delete=models.CASCADE,
        related_name="organizers",
        null=True,
    )
    organization = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField(
        ("Avatar"),
        upload_to="organizers/avatars/",
        height_field=None,
        width_field=None,
        max_length=255,
        null=True,
    )

    class Meta:
        """Meta options for the Organizer model."""

        db_table = "organizers"
        verbose_name = "Organizer"
        verbose_name_plural = "Organizers"

    def __str__(self):
        """String representation of the Organizer."""
        return self.organization

    def get_absolute_url(self):
        """Returns the absolute URL for the Organizer detail view."""
        return reverse("Organizer_detail", kwargs={"pk": self.pk})


class SocialLinks(TimestampedModel):
    """Social Links model."""

    social_name = models.CharField(max_length=50, null=True)
    social_link = models.URLField(max_length=200, null=True)
    organizer = models.ForeignKey(
        Organizers,
        on_delete=models.DO_NOTHING,
        related_name="organizers_social_accounts",
        null=True,
    )

    class Meta:
        """meta options."""

        ordering = ["social_name"]
        db_table = "Social Link "
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self) -> str:
        """Return social name and social link."""
        if self.social_name:
            return f"{self.social_name} ({self.social_link})"


class AttendanceEmails(TimestampedModel):
    """Model for storing event attendance emails."""

    email = models.EmailField(null=True, unique=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="event_attendance_emails",
    )
    is_given_feedback = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class AttendeeCSVUpload(TimestampedModel):
    """Model to handle CSV upload for attendees."""

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="csv_uploads",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="attendee_uploads",
    )
    csv_file = models.FileField(
        upload_to="attendee_uploads/",
        help_text=(
            "Upload a CSV file with attendee data "
            "(first_name, last_name, email, organization)"
        ),
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True, blank=True)
    success_count = models.IntegerField(default=0)
    error_count = models.IntegerField(default=0)
    error_log = models.TextField(blank=True)

    class Meta:
        verbose_name = "Attendee CSV Upload"
        verbose_name_plural = "Attendee CSV Uploads"
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"CSV Upload for {self.event} by {self.organizer.email}"

    def process_csv(self):
        process_csv_file(self, AttendanceEmails)
