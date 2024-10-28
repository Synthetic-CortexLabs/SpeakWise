from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event
from talks.models import Talk

# Create your models here.
User = get_user_model()

class Feedback(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE, related_name='reviews')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    speaker_expertise = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    depth_of_topic = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    relevancy = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    value_or_impact = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Feedback by {self.reviewer.user.username} for {self.talk.title}"

     def average_score(self):
        total = self.speaker_expertise + self.depth_of_topic + self.relevancy + self.value_or_impact
        return total / 4
