import logging
from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event
from talks.models import Talks

# Set up a logger for your application
logger = logging.getLogger(__name__)

# Create your models here.
User = get_user_model()

class Feedback(models.Model):

    NUM_STARS = [
        (1,1),
        (2,2),
        (3,3),
        (4,4)
        (5,5),
    ]
    talk = models.ForeignKey(Talks, on_delete=models.CASCADE, related_name='reviews')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    speaker_expertise = models.IntegerField(choices=NUM_STARS, default=NUM_STARS[0][0])
    depth_of_topic = models.IntegerField(choices=NUM_STARS, default=NUM_STARS[0][0])
    relevancy = models.IntegerField(choices=NUM_STARS, default=NUM_STARS[0][0])
    value_or_impact = models.IntegerField(choices=NUM_STARS, default=NUM_STARS[0][0])
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedback"

    def __str__(self):
        return f"Feedback by {self.reviewer.user.username} for {self.talk.title} at  {self.event.title} event"

    def average_score(self):
    try:
        total = (
            self.speaker_expertise +
            self.depth_of_topic +
            self.relevancy +
            self.value_or_impact
        )
        
        # Return None or a message if the total score is zero to avoid division
        if total == 0:
            logger.warning("Total score is zero; average cannot be calculated.")
            return None
        
        return total / 4
    except (TypeError, ValueError) as e:
        # Log the exception with a warning message
        logger.error(f"An error occurred while calculating average score: {e}")
        return None
