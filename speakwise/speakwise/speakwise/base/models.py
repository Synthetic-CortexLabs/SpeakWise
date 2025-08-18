"""Base models for the SpeakWise application."""

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

PHONE_REGEX = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),
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
        if not self.social_url.startswith(("https://", "http://")):
            msg = "Social URL must start with https:// or http://"

            raise ValidationError(msg)


# Team member upload directory
TEAM_UPLOAD_DIR = "team/avatars/"


class TeamMember(TimestampedModel):
    """Team Member Model for the SpeakWise application.

    This model is used to store team member information that will be
    displayed on the "Meet Our Team" page.
    """

    name = models.CharField(
        max_length=100,
        help_text="Full name of the team member",
    )
    role = models.CharField(
        max_length=100,
        help_text="Job title or role in the company",
    )
    short_bio = models.TextField(
        max_length=500,
        help_text="Brief biography of the team member",
    )
    avatar = models.ImageField(
        upload_to=TEAM_UPLOAD_DIR,
        blank=True,
        null=True,
        help_text="Profile picture of the team member",
    )

    # Social media links
    twitter_url = models.URLField(blank=True, help_text="Twitter profile URL")
    linkedin_url = models.URLField(
        blank=True,
        help_text="LinkedIn profile URL",
    )
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")
    website_url = models.URLField(
        blank=True,
        help_text="Personal website URL",
    )

    # Display settings
    is_active = models.BooleanField(
        default=True,
        help_text="Show this team member on the website",
    )
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which to display team members",
    )

    class Meta:
        """Meta class for team member model configuration."""

        db_table = "team_member"
        ordering = ["display_order", "name"]
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        """Returns the team member's name."""
        return f"{self.name} - {self.role}"

    @property
    def avatar_url(self):
        """Returns the full URL for the avatar image."""
        if self.avatar:
            return self.avatar.url
        return None
