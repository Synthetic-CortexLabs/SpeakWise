"""Base models for the SpeakWise application."""

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

PHONE_REGEX = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)


class TimestampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating 'created' and 'modified' fields.
    """

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        """Metadata options for the model."""

        abstract = True


class SocialLink(TimestampedModel):
    """Abstract base model for storing social media links.

    Base class that provides common fields and functionality for
    social media links across different model types.

    Attributes:
        social_name (CharField): Name of social media platform
        social_url (URLField): Full URL to social media profile
        is_active (BooleanField): Whether link is currently active
        display_order (IntegerField): Order for display sorting
    """
    social_name = models.CharField(max_length=50)
    social_url = models.URLField()
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["display_order"]

    def __str__(self) -> str:
        if self.social_name:
            return self.social_name
        return "Social Handle Name"

    def clean(self) -> None:
        """Validate social link data."""
        if not self.social_url.startswith(("http://", "https://")):
            msg = "Social URL must start with http:// or https://"
            raise ValidationError(msg)
