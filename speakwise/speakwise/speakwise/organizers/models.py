"""Organizer models."""

from django.db import models
from django.urls import reverse

from speakwise.base.models import TimestampedModel, SocialLink
from speakwise.events.models import Event
from speakwise.users.models import User


class OrganizersSocialLinks(SocialLink):
    """organizers social links."""

    organizer = models.ForeignKey(
        "organizers.Organizers",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="organizers_social_accounts",
    )


class Organizers(TimestampedModel):
    """Organizer model."""

    user_id = models.OneToOneField(User, on_delete=models.CASCADE) #
    # organizer must be a user.
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
