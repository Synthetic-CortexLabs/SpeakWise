"""teams models."""

from django.db import models
from speakwise.base.models import TimestampedModel, SocialLink


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

    class Meta:
        """meta options."""

        ordering = ["display_order", "name"]


class TeamSocial(SocialLink):
    """team member social link."""

    team = models.ForeignKey(
        TeamMember,
        related_name="social_links",
        on_delete=models.CASCADE,
        help_text="Team member associated with this social link",
    )
