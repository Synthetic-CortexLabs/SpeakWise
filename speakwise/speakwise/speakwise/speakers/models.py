"""Speakers models."""

from base.models import SocialLink
from base.models import TimestampedModel
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.urls import reverse

from speakwise.events.models import Event
from speakwise.feedbacks.models import Feedback

# Speakers file upload directory
SPEAKERS_UPLOAD_DIR = "speakers/avatars/"


# this are skill_tags the  Speakers can add to their profile eg. Python, Django, React, etc
class SkillTag(TimestampedModel):
    """SkillTag Model for the SpeakWise application.

    This model is used to store the speaker's skill tags.
    """

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "skill_tag"

    def __str__(self):
        return self.name


class SpeakerProfile(TimestampedModel):
    """Speaker Model for the SpeakWise application.

    This model is used to store the speaker's profile information.
    """

    speaker_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="speaker_profile",
    )

    events_spoken = models.ManyToManyField(Event, blank=True, related_name="speakers")
    organization = models.CharField(max_length=255, blank=True)
    short_bio = models.CharField(max_length=255, blank=True)
    long_bio = models.TextField()
    country = models.CharField(max_length=255, blank=True)
    # social_handle = models.ForeignKey(Handles, on_delete=models.DO_NOTHING, null=True)
    avatar = models.ImageField(upload_to=SPEAKERS_UPLOAD_DIR, blank=True)
    skill_tags = models.ManyToManyField(SkillTag, blank=True)

    class Meta:
        """
        Meta class for speaker profile model configuration.
        Specifies custom database table name.
        """

        db_table = "speaker_profile"

    def get_absolute_url(self):
        """Returns the absolute URL for the speaker profile detail view."""
        return reverse("speaker_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """Returns the speaker's full name."""
        return f"{self.speaker_user.get_full_name()}"


# The Code below is the speakerDashboard


class SpeakerDashboard(TimestampedModel):
    """SpeakerDashboard Model for the SpeakWise application.
    This model is used to store and manage speaker dashboard information including
    feedback and profile relationships.

    Attributes:
        speaker_profile (ForeignKey): Reference to SpeakerProfile
        feedback (ForeignKey): Reference to Feedback model
    """

    speaker_profile = models.ForeignKey(
        SpeakerProfile,
        on_delete=models.CASCADE,
        related_name="speaker_dashboard",
    )
    feedback = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        related_name="speaker_dashboard",
    )

    class Meta:
        """Meta class for speaker dashboard model configuration."""

        db_table = "speaker_dashboard"

    def get_absolute_url(self):
        """Returns the absolute URL for the speaker dashboard detail view."""

        return reverse("speaker_detail", kwargs={"pk": self.pk})

    @property
    def feedback_rate_per_conference(self):
        """Calculates average feedback ratings grouped by conference.

        Returns:
            dict: Conference names as keys and their average ratings as values
        """
        # Get all events the speaker has participated in
        speaker_events = self.speaker_profile.events_spoken.all()
        conference_feedback = {}

        # Group events by conference and calculate average feedback
        for event in speaker_events:
            conference_name = (
                event.conference.name
                if hasattr(event, "conference")
                else "No Conference"
            )
            feedbacks = Feedback.objects.filter(
                event=event,
                speaker=self.speaker_profile,
            )
            if feedbacks.exists():
                avg_rate = feedbacks.aggregate(models.Avg("rating"))["rating__avg"]
                if conference_name in conference_feedback:
                    conference_feedback[conference_name].append(round(avg_rate, 2))
                else:
                    conference_feedback[conference_name] = [round(avg_rate, 2)]
        # Calculate average for each conference
        return {
            conf: round(sum(rates) / len(rates), 2)
            for conf, rates in conference_feedback.items()
        }

    @property
    def full_name(self):
        """Returns the speaker's full name by combining first and last name."""
        return f"{self.speaker_profile.speaker_user.first_name} {self.speaker_profile.speaker_user.last_name}"

    @property
    def total_events(self):
        """Returns the total number of events the speaker has participated in."""
        return self.speaker_profile.events_spoken.count()

    @property
    def average_feedback_rating(self):
        """Returns the speaker's average feedback rating across all events."""
        feedbacks = Feedback.objects.filter(speaker=self.speaker_profile)
        if feedbacks.exists():
            return round(feedbacks.aggregate(models.Avg("rating"))["rating__avg"], 2)
        return 0.0


class Handles(TimestampedModel):
    """
    A model representing social media handles for speakers.
    This model stores social media account information (name and URL) associated with speakers.
    Inherits from TimestampedModel to track creation and modification times.
    Attributes:
        social_name (CharField): Name of the social media platform (up to 50 chars)
        social_link (URLField): URL to the social media profile (up to 200 chars)
        speakers (ForeignKey): Reference to associated Speaker model
    Meta:
        ordering: Ordered by social media platform name
        db_table: "Handles"
    """

    social_name = models.CharField(max_length=50, null=True)  # noqa: DJ001
    social_link = models.URLField(max_length=200, null=True)  # noqa: DJ001

    speaker = models.ForeignKey(
        SpeakerProfile,
        on_delete=models.DO_NOTHING,
        related_name="speakers_social_accounts",
        null=True,
    )

    class Meta:
        """Meta options for the Handles model."""

        ordering = ["social_name"]
        db_table = "Handles"
        verbose_name = "Social Media Handle"
        verbose_name_plural = "Social Media Handles"

    def __str__(self) -> str:
        """Return social media platform name and URL."""
        if self.social_name:
            return self.social_name
        return "Social Media Handle"


class SpeakerSocialLink(SocialLink):
    """Model for speaker's social media profiles.

    Extends the base SocialLink model to associate social media
    links specifically with speakers.

    Attributes:
        speaker (ForeignKey): Reference to associated SpeakerProfile
    """

    speaker = models.ForeignKey(
        SpeakerProfile,
        on_delete=models.CASCADE,
        related_name="social_links",
    )

    class Meta:
        """Meta options for the SpeakerSocialLink model."""

        verbose_name = "Speaker Social Link"
        verbose_name_plural = "Speaker Social Links"
        unique_together = ["speaker", "social_name"]
        ordering = ["display_order", "social_name"]

    def __str__(self) -> str:
        """Return a string representation of the speaker's social media profile."""
        return f"{self.speaker}'s {self.social_name} link"

    def clean(self) -> None:
        """Speaker-specific validation."""
        super().clean()
        if (
            SpeakerSocialLink.objects.filter(
                speaker=self.speaker,
                social_name=self.social_name,
            )
            .exclude(id=self.id)
            .exists()
        ):
            msg = f"Speaker already has a {self.social_name} profile linked"
            raise ValidationError(
                msg,
            )
