"""user role choices."""

from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class UserRoles(TextChoices):
    """User roles."""

    ADMIN = "admin", _("Admin")
    ATTENDEE = "attendee", _("Attendee")
    ORGANIZER = "organizer", _("Organizer")
    SPEAKER = "speaker", _("Speaker")
