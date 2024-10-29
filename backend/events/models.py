"""Event models."""

from django.db import models
from organizers.models import Organizer
from speakers.models import Speaker
from base.models import TimestampedModel
from django.utils import timezone

# Create your models here.


class Event(TimestampedModel):
    """
    Represents an event.

    Attributes:path("encounters/", views.EncounterListView.as_view()),
    # path("encounters/<int:pk>/", views.EncounterDetailView.as_view()),
        title (str): The event's title.
        description (str): A detailed description of the event.
        start_date (datetime): When the event starts.
        end_date (datetime): When the event ends.
        organizers (ManyToManyField): Organizers of the event.
        speakers (ManyToManyField): Speakers at the event.
        created_at (datetime): When the event was created.
        updated_at (datetime): When the event was last updated.
        location (str): The event's location.

    Methods:
        __str__(): Returns the event's title.

    """

    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    organizers = models.ManyToManyField(Organizer, related_name="events")
    speakers = models.ManyToManyField(Speaker, related_name="events")
    location = models.CharField(max_length=100, null=True)

    class Meta:
        """Meta options."""

        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["start_date"]

    def __str__(self):
        """Return the event's title."""
        return self.title
