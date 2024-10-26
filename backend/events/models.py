from django.db import models
from organizers.models import Organizer
from speakers.models import Speaker

# Create your models here.


class Event(models.Model):
    """
    Represents an event.

    Attributes:
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
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizers = models.ManyToManyField(Organizer, related_name="events")
    speakers = models.ManyToManyField(Speaker, related_name="events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["start_date"]

    def __str__(self):
        return self.title
