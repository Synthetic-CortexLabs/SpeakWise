"""This module contains the model for the talks app."""

from base.models import TimestampedModel
from django.db import models

from speakwise.events.models import Event
from speakwise.speakers.models import Speaker


class Talks(TimestampedModel):
    """
        event_id (ForeignKey): Reference to the associated event.
        start_time (DateTimeField): The start time of the talk.
        end_time (DateTimeField): The end time of the talk.
        speaker_id (ManyToManyField): Reference to the associated speakers.
    Methods:
        __str__: Returns the title of the talk.

        Returns:
            _type_: _description_
    """

    event_id = models.ForeignKey(
        Event,
        on_delete=models.DO_NOTHING,
        null=True,
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    speaker_id = models.ManyToManyField(Speaker)

    class Meta:
        app_label = "talks"

    def __str__(self):
        """Return the title of the talk."""
        return self.title
