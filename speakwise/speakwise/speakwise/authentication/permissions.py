"""Authentication permissions module."""

from rest_framework.permissions import BasePermission


class IsAttendee(BasePermission):
    """
    Permission that allows access to attendees only.
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if not request.user or not request.user.is_authenticated:
            return False

        # Check if user has a role and if role display is attendee
        if not hasattr(request.user, "role") or not request.user.role:
            return False

        return request.user.role.display == "attendee"


class IsSpeaker(BasePermission):
    """
    Permission that allows access to speakers only.
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if not request.user or not request.user.is_authenticated:
            return False

        # Check if user has a role and if role display is speaker
        if not hasattr(request.user, "role") or not request.user.role:
            return False

        return request.user.role.display == "speaker"


class IsOrganizer(BasePermission):
    """
    Permission that allows access to organizers only.
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if not request.user or not request.user.is_authenticated:
            return False

        # Check if user has a role and if role display is organizer
        if not hasattr(request.user, "role") or not request.user.role:
            return False

        return request.user.role.display == "organizer"


class IsSpeakerOrOrganizerOrAdmin(BasePermission):
    """
    Permission that allows access to speakers, organizers, and admins.
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if not request.user or not request.user.is_authenticated:
            return False

        # Check if user has a role and if role display is organizer or admin
        if not hasattr(request.user, "role") or not request.user.role:
            return False

        return request.user.role.display in ["speaker", "organizer", "admin"]


class IsOrganizerOrAdmin(BasePermission):
    """
    Permission that allows access to organizers and admins only.
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if not request.user or not request.user.is_authenticated:
            return False

        # Check if user has a role and if role display is organizer or admin
        if not hasattr(request.user, "role") or not request.user.role:
            return False

        return request.user.role.display in ["organizer", "admin"]


class IsOwnerOrReadOnly(BasePermission):
    """
    Permission that allows owners to edit their own objects,
    and read-only access to others.
    """

    def has_object_permission(self, request, view, obj):
        """Check if user has object-level permission."""
        # Read permissions for any authenticated user
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Write permissions only to the owner
        return obj.user == request.user


class IsAuthenticatedUser(BasePermission):
    """
    Permission that allows access to all authenticated users: attendees, speakers,
    organizers, and admins.
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if not request.user or not request.user.is_authenticated:
            return False

        # Check if user has a role
        if not hasattr(request.user, "role") or not request.user.role:
            return False

        # Allow access to any authenticated user with a valid role
        return request.user.role.display in [
            "attendee",
            "speaker",
            "organizer",
            "admin",
        ]
