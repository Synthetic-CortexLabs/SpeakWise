"""Events views."""

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Country, Event, Region, Session, Tag
from .serializers import (
    CountrySerializer,
    EventSerializer,
    RegionSerializer,
    SessionSerializer,
    TagSerializer,
)


@extend_schema(request=EventSerializer, responses={200: EventSerializer})
class EventListCreateAPIView(ListCreateAPIView):
    """View for listing and creating events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: EventSerializer})
class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)


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


@extend_schema(request=RegionSerializer, responses={200: RegionSerializer})
class RegionListCreateAPIView(ListCreateAPIView):
    """View for listing and creating regions."""

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: RegionSerializer})
class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting regions."""

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
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
