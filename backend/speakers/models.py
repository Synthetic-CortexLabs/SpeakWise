from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import TimestampedModel


# Create your models here.
class Speaker(TimestampedModel):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="speakers/avatars/")

    class Meta:
        db_table = "speakers"
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"

    def __str__(self):
        return self.user_id.username

    def get_absolute_url(self):
        return reverse("speaker_detail", kwargs={"pk": self.pk})