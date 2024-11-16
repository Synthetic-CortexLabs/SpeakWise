"""user choices file."""

from django.db.models import TextChoices


class UserRole(TextChoices):
    """User roles choices."""

    ORGANIZER = "Organizer", "Organizer"
    SPEAKER = "Speaker", "Speaker"
    ATTENDEE = "Attendee", "Attendee"
