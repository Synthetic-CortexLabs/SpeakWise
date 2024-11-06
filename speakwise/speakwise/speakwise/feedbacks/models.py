# Create your models here.
from django import models
from base.models import TimestampedModel
from talks.models import Talks


class Feedback(TimestampedModel):
    """
        Feedback Model
    """
    #attendee = models.ForeignKey()
    talk = models.ForeignKey(Talks,on_delete=models.CASCADE)
    overall_rating = models.PositiveIntegerField()
    engagement  = models.PositiveIntegerField()
    clarity  = models.PositiveIntegerField()
    content_depth  = models.PositiveIntegerField()
    speaker_knowledge  = models.PositiveIntegerField()
    practical_relevance  = models.PositiveIntegerField()
    comments  = models.TextField()
    is_anonymous = models.BooleanField()
    is_editable = models.BoleanField(default=True)

    class Meta:
        db_table = "feedbacks"
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


    def __str__(self):
        return self.overall_rating




