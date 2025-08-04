"""Events views."""

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from speakwise.authentication.permissions import IsAuthenticatedUser
from speakwise.organizers.models import Organizers
from speakwise.events.models import Country, Event, Session, Tag
from speakwise.events.serializers import (
    CountrySerializer,
    EventSerializer,
    SessionSerializer,
    TagSerializer,
)


def is_organizer_or_admin(user):
    """Helper method to check if user is organizer or admin."""
    return (
        hasattr(user, "role")
        and user.role
        and user.role.display in ["organizer", "admin"]
    )


def is_organizer(user):
    """Helper method to check if user is organizer."""
    return hasattr(user, "role") and user.role and user.role.display == "organizer"


@extend_schema(request=EventSerializer, responses={200: EventSerializer})
class EventListCreateAPIView(ListCreateAPIView):
    """View for listing and creating events."""

    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedUser,)

    def get_queryset(self):
        """
        Return all events for any authenticated user.
        For organizers, only show their own events for editing.
        """
        user = self.request.user
        if user.is_authenticated:
            # Check if user is an organizer - if so, show only their events
            if is_organizer(user):
                try:
                    organizer = Organizers.objects.get(user_id=user)
                    return Event.objects.filter(organizer=organizer)
                except Organizers.DoesNotExist:
                    return Event.objects.none()
            # For all other authenticated users, show all events
            return Event.objects.all()
        return Event.objects.none()

    def perform_create(self, serializer):
        """Set the organizer when creating an event."""
        user = self.request.user

        # Only organizers and admins can create events
        if is_organizer_or_admin(user):
            try:
                organizer = Organizers.objects.get(user_id=user)
                serializer.save(organizer=organizer)
            except Organizers.DoesNotExist:
                # Create organizer profile if it doesn't exist
                organizer = Organizers.objects.create(
                    user_id=user,
                    organization=(
                        f"{user.first_name or ''} {user.last_name or ''}".strip()
                        or getattr(user, "username", None)
                        or getattr(user, "email", "Organizer")
                    ),
                )
                serializer.save(organizer=organizer)
        else:
            # Return permission denied for non-organizers
            raise PermissionDenied(
                detail="Only organizers and admins can create events."
            )


@extend_schema(responses={200: EventSerializer})
class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting events."""

    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedUser,)

    def get_queryset(self):
        """
        Return all events for any authenticated user.
        For organizers, only show their own events for editing.
        """
        user = self.request.user
        if user.is_authenticated:
            # For read operations, show all events
            if self.request.method == "GET":
                return Event.objects.all()

            # For write operations, only allow organizers to modify their own
            # events
            if is_organizer_or_admin(user):
                try:
                    organizer = Organizers.objects.get(user_id=user)
                    return Event.objects.filter(organizer=organizer)
                except Organizers.DoesNotExist:
                    return Event.objects.none()
            return Event.objects.none()
        return Event.objects.none()


@extend_schema(request=SessionSerializer, responses={200: SessionSerializer})
class SessionListCreateAPIView(ListCreateAPIView):
    """View for listing and creating sessions."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: SessionSerializer})
class SessionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting sessions."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (AllowAny,)


@extend_schema(request=CountrySerializer, responses={200: CountrySerializer})
class CountryListCreateAPIView(ListCreateAPIView):
    """View for listing and creating countries."""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: CountrySerializer})
class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting countries."""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


@extend_schema(request=TagSerializer, responses={200: TagSerializer})
class TagListCreateAPIView(ListCreateAPIView):
    """View for listing and creating tags."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: TagSerializer})
class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting tags."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: EventSerializer})
class EventDetailAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving event details with extended information."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)


# Function-based views for speaker and session management


@api_view(["GET"])
@permission_classes([AllowAny])
def list_event_speakers(request, event_id):
    """List speakers for a specific event."""
    get_object_or_404(Event, id=event_id)
    # This would need proper implementation based on your
    # speaker-event relationship
    return Response({"speakers": [], "event_id": event_id})


@api_view(["POST"])
@permission_classes([AllowAny])
def add_speaker_to_event(request, event_id):
    """Add a speaker to an event."""
    get_object_or_404(Event, id=event_id)
    # This would need proper implementation
    return Response(
        {"message": "Speaker added to event"},
        status=status.HTTP_201_CREATED,
    )


@api_view(["DELETE"])
@permission_classes([AllowAny])
def remove_speaker_from_event(request, event_id):
    """Remove a speaker from an event."""
    get_object_or_404(Event, id=event_id)
    # This would need proper implementation
    return Response(
        {"message": "Speaker removed from event"},
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def list_event_sessions(request, event_id):
    """List sessions for a specific event."""
    event = get_object_or_404(Event, id=event_id)
    sessions = Session.objects.filter(event=event)
    serializer = SessionSerializer(sessions, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def create_session_with_speaker(request, event_id):
    """Create a session with speaker assignment."""
    get_object_or_404(Event, id=event_id)
    # This would need proper implementation based on your data structure
    return Response(
        {"message": "Session created"},
        status=status.HTTP_201_CREATED,
    )
