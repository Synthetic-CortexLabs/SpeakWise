from typing import ClassVar

from speakwise.base.models import TimestampedModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from .choices import UserRoles as ROLE_CHOICES


class User(AbstractUser):

    first_name = models.CharField(max_length=255, help_text="First name")
    last_name = models.CharField(max_length=255, help_text="Last name ")
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.OneToOneField(
        "users.UserRole",
        on_delete=models.CASCADE,
        related_name="users",
        help_text="User role",
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def __str__(self) -> str:
        """Return user's full name."""
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view."""
        return reverse("users:detail", kwargs={"pk": self.id})


class UserRole(TimestampedModel):
    """USER ROLE MODEL."""

    display = models.CharField(
        max_length=255,
        help_text="User role display name",
        choices=ROLE_CHOICES.choices,
        null=True,
    )
