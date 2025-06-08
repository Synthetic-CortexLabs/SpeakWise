"""Talks views module."""

from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from speakwise.talks.models import Talks
from speakwise.talks.serializers import TalkSerializer
from speakwise.authentication.permissions import (
    IsSpeakerOrOrganizerOrAdmin,
    IsOrganizerOrAdmin,
)
from speakwise.users.choices import UserRoles


@extend_schema(request=TalkSerializer, responses={200: TalkSerializer})
class TalkListCreateView(generics.ListCreateAPIView):
    """View to list all talks and create a new talk."""

    queryset = Talks.objects.all()
    serializer_class = TalkSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        POST request is available only to speakers, organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsSpeakerOrOrganizerOrAdmin()]


class TalkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a talk."""

    queryset = Talks.objects.all()
    serializer_class = TalkSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        PUT, PATCH requests are available to the speaker who created the talk,
        or organizers and admins
        DELETE request is available only to organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        if self.request.method == "DELETE":
            return [IsOrganizerOrAdmin()]
        return [IsSpeakerOrOrganizerOrAdmin()]

    def check_object_permissions(self, request, obj):
        """Check if speaker has permission to modify their own talk."""
        super().check_object_permissions(request, obj)

        # If the user is an organizer or admin, they can edit/delete any talk
        if (
            hasattr(request.user, "role")
            and request.user.role
            and request.user.role.display in [UserRoles.ORGANIZER, UserRoles.ADMIN]
        ):
            return

        # If the user is the speaker who created this talk, allow edit access
        if obj.speaker and obj.speaker.user == request.user:
            return

        # Otherwise, deny permission
        self.permission_denied(
            request,
            message="You don't have permission to modify this talk.",
        )
