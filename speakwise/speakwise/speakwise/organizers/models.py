# Create your models here.
from django.db import models
from django.urls import reverse

from speakwise.base.models import TimestampedModel
from speakwise.events.models import Event
from speakwise.users.models import User


class SocialLinks(models.Model):
    social_name = models.CharField(max_length=50, blank=True)
    social_link = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ["social_name"]
        db_table = "Social Link "
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self) -> str:
        if self.social_name:
            return f"{self.social_name} ({self.social_link})"
        return None  # noqa: PLE0307


class Organizers(TimestampedModel):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    socials = models.ForeignKey(
        SocialLinks,
        verbose_name=("social links"),
        on_delete=models.CASCADE,
    )
    events = models.ForeignKey(
        Event,
        verbose_name=("events"),
        on_delete=models.CASCADE,
        related_name="organizers",
    )
    organization = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField(
        ("Avatar"),
        upload_to="organizers/avatars/",
        height_field=None,
        width_field=None,
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        """Meta options for the Organizer model."""

        db_table = "organizers"
        verbose_name = "Organizer"
        verbose_name_plural = "Organizers"

    def __str__(self):
        """String representation of the Organizer."""
        return self.organization

    def get_absolute_url(self):
        """Returns the absolute URL for the Organizer detail view."""
        return reverse("Organizer_detail", kwargs={"pk": self.pk})
