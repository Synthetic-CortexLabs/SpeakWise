import logging
from django.db import models
from django.contrib.auth import get_user_model
from base.models import TimestampedModel
from events.models import Event
from talks.models import Talks

# Set up a logger for your application
logger = logging.getLogger(__name__)

# Create your models here.
User = get_user_model()


class Feedback(models.Model):
    """
    Feedback Model
    This model represents feedback given by a reviewer for a specific talk at an event.
    It includes ratings on various aspects such as speaker expertise, depth of topic, relevancy, and value or impact,
    as well as optional comments.
    Attributes:
        NUM_STARS (list of tuples): Choices for rating fields, ranging from 1 to 5.
        talk (ForeignKey): Reference to the Talks model, representing the talk being reviewed.
        event (ForeignKey): Reference to the Event model, representing the event where the talk was given.
        reviewer (ForeignKey): Reference to the User model, representing the reviewer.
        speaker_expertise (IntegerField): Rating for the speaker's expertise, with choices from NUM_STARS.
        depth_of_topic (IntegerField): Rating for the depth of the topic, with choices from NUM_STARS.
        relevancy (IntegerField): Rating for the relevancy of the talk, with choices from NUM_STARS.
        value_or_impact (IntegerField): Rating for the value or impact of the talk, with choices from NUM_STARS.
        comments (TextField): Optional comments provided by the reviewer.
    Meta:
        verbose_name (str): Human-readable name for the model in singular form.
        verbose_name_plural (str): Human-readable name for the model in plural form.
    Methods:
        __str__(): Returns a string representation of the feedback, including the reviewer's username,
                   the talk title, and the event title.
        average_score(): Calculates and returns the average score of the ratings.
                         Returns None if the total score is zero or if an error occurs during calculation.
    """

    NUM_STARS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    talk = models.ForeignKey(Talks, on_delete=models.CASCADE, related_name="reviews")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
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
                self.speaker_expertise
                + self.depth_of_topic
                + self.relevancy
                + self.value_or_impact
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


class FeedbackTrend(TimestampedModel):
    talk_id = models.ForeignKey(Talks, on_delete=models.CASCADE, related_name="trends")
    date = models.DateField()
    average_daily_rating = models.FloatField()
    daily_feedback_count = models.PositiveIntegerField()
    positive_feedback_count = models.PositiveIntegerField()

    indexes = [
        models.Index(fields=["talk_id", "date"]),
    ]
    unique_together = ("talk_id", "date")  # Ensures unique trends per talk per date
    ordering = ["-date"]

    def __str__(self):
        return f"{self.date} - Avg Rating: {self.average_daily_rating} - Feedback Count: {self.daily_feedback_count}"
