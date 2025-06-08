"""Custom permission classes for role-based access control."""

from rest_framework.permissions import BasePermission

from speakwise.users.choices import UserRoles


class IsAttendee(BasePermission):
    """
    Permission class to allow only users with attendee role.
    """

    def has_permission(self, request, view):
        """Check if user has attendee role."""
        return (
            request.user.is_authenticated
            and request.user.role is not None
            and request.user.role.display == UserRoles.ATTENDEE
        )


class IsSpeaker(BasePermission):
    """
    Permission class to allow only users with speaker role.
    """

    def has_permission(self, request, view):
        """Check if user has speaker role."""
        return (
            request.user.is_authenticated
            and request.user.role is not None
            and request.user.role.display == UserRoles.SPEAKER
        )


class IsOrganizer(BasePermission):
    """
    Permission class to allow only users with organizer role.
    """

    def has_permission(self, request, view):
        """Check if user has organizer role."""
        return (
            request.user.is_authenticated
            and request.user.role is not None
            and request.user.role.display == UserRoles.ORGANIZER
        )


class IsAdmin(BasePermission):
    """
    Permission class to allow only users with admin role.
    """

    def has_permission(self, request, view):
        """Check if user has admin role."""
        return (
            request.user.is_authenticated
            and request.user.role is not None
            and request.user.role.display == UserRoles.ADMIN
        )


class IsOrganizerOrAdmin(BasePermission):
    """
    Permission class to allow users with either organizer or admin roles.
    """

    def has_permission(self, request, view):
        """Check if user has organizer or admin role."""
        return (
            request.user.is_authenticated
            and request.user.role is not None
            and request.user.role.display in [UserRoles.ORGANIZER, UserRoles.ADMIN]
        )


class IsSpeakerOrOrganizerOrAdmin(BasePermission):
    """
    Permission class to allow users with either speaker, organizer, or admin roles.
    """

    def has_permission(self, request, view):
        """Check if user has speaker, organizer, or admin role."""
        return (
            request.user.is_authenticated
            and request.user.role is not None
            and request.user.role.display
            in [UserRoles.SPEAKER, UserRoles.ORGANIZER, UserRoles.ADMIN]
        )
