"""Custom managers for the User model."""

from datetime import timedelta
from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models
from django.db.models import Q
from django.utils import timezone

if TYPE_CHECKING:
    from .models import User  # noqa: F401


class UserManager(DjangoUserManager["User"]):
    """Custom manager for the User model."""

    def create(self, email: str, password: str | None, **extra_fields):
        """Create and save a user with the given email and password."""
        if not email:
            msg = "The given email must be set"
            raise ValueError(msg)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str | None = None, **extra_fields):  # type: ignore[override]
        """Create and save a regular user with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self.create(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str | None = None, **extra_fields):  # type: ignore[override]
        """Create and save a superuser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            msg = "Superuser must have is_staff=True."
            raise ValueError(msg)
        if extra_fields.get("is_superuser") is not True:
            msg = "Superuser must have is_superuser=True."
            raise ValueError(msg)

        return self.create(email, password, **extra_fields)


class BaseInvitationManager(models.Manager):
    """Custom manager for the Invite model."""

    def all_expired(self):
        """Return all expired invitations."""
        return self.filter(self.expired_q())

    def all_valid(self):
        """Return all valid invitations."""
        return self.exclude(self.expired_q())

    def expired_q(self):
        """Return the query for expired invitations."""
        sent_threshold = timezone.now() - timedelta(days=settings.INVITATION_EXPIRY)
        q = Q(accepted=True) | Q(sent__lt=sent_threshold)
        return q

    def delete_expired_confirmations(self):
        """Delete all expired confirmations."""
        self.all_expired().delete()
