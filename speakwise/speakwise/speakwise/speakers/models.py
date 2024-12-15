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

    @property
    def feedback_rate_per_conference(self):
        # Get all events the speaker has participated in
        speaker_events = self.event.all()
        conference_feedback = {}

        # Group events by conference and calculate average feedback
        for event in speaker_events:
            conference_name = event.conference.name if event.conference else "No Conference"
            feedbacks = Feedback.objects.filter(event=event, speaker=self)
            if (feedbacks.exists()):
                avg_rate = feedbacks.aggregate(models.Avg('rating'))['rating__avg']
                if conference_name in conference_feedback:
                    conference_feedback[conference_name].append(round(avg_rate, 2))
                else:
                    conference_feedback[conference_name] = [round(avg_rate, 2)]
        # Calculate average for each conference
        return {conf: round(sum(rates)/len(rates), 2) 
                for conf, rates in conference_feedback.items()}

    @property
    def full_name(self):
        """Returns the speaker's full name by combining first and last name."""
        return f"{self.speaker_user.first_name} {self.speaker_user.last_name}"

    @property
    def total_events(self):
        """Returns the total number of events the speaker has participated in."""
        return self.event.count()

    @property
    def average_feedback_rating(self):
        """Returns the speaker's average feedback rating across all events."""
        feedbacks = Feedback.objects.filter(speaker=self)
        if feedbacks.exists():
            return round(feedbacks.aggregate(models.Avg('rating'))['rating__avg'], 2)
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


