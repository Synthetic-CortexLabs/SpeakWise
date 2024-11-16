from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from speakwise.base.models import PHONE_REGEX
from speakwise.base.models import TimestampedModel

from .choices import UserRole
from .managers import UserManager


class User(AbstractUser, TimestampedModel):
    """
    Default custom user model for speakwise.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    username = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(_("email address"), unique=True)
    phone = CharField(
        _("Phone Number"),
        blank=True,
        max_length=255,
        validators=[PHONE_REGEX],
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"pk": self.id})

    class Role(TimestampedModel):
        """user roles model."""

        display = CharField(max_length=255, choices=UserRole.choices)
