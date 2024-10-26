from django.db import models

# Create your models here.


class Talks(models.Model):
    """
    A Django model representing a talk or presentation.
    Attributes:
        title (str): The title of the talk.
        speaker (str): The name of the speaker.
        duration (int): The duration of the talk in minutes.
        date (date): The date of the talk.
        time (time): The time of the talk.
        location (str): The location where the talk will be held.
        description (str): A detailed description of the talk.
    """
    """
        Returns the string representation of the Talks instance, which is the title of the talk.
        Returns:
            str: The title of the talk.
    """

    event_id = models.ForeignKey("Event", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    speaker_id = models.ManyToManyField("Speaker")

    def __str__(self):
        return self.title
