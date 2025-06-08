"""Events views."""

from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Country
from .models import Event
from .models import Region
from .models import Session
from speakwise.speakers.models import SpeakerProfile
from speakwise.speakers.serializers import SpeakerProfileSerializer
from .serializers import CountrySerializer
from .serializers import EventSerializer
from .serializers import RegionSerializer
from .serializers import SessionSerializer
from .serializers import TagSerializer
from .serializers_extended import EventWithGuestSpeakersSerializer
from .models import Tag
from speakwise.authentication.permissions import (
    IsOrganizer,
    IsSpeaker,
    IsOrganizerOrAdmin,
    IsSpeakerOrOrganizerOrAdmin,
)
from speakwise.users.choices import UserRoles


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

    def get_queryset(self):
        """Filter countries by region if region parameter is provided."""
        queryset = Country.objects.all()
        region_id = self.request.query_params.get("region")

        if region_id:
            queryset = queryset.filter(region_id=region_id)

        return queryset


@extend_schema(responses={200: CountrySerializer})
class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting countries."""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


@extend_schema(request=EventSerializer, responses={200: EventSerializer})
class EventListCreateAPIView(ListCreateAPIView):
    """View for listing and creating events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        POST request is available only to organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsOrganizerOrAdmin()]


@extend_schema(responses={200: EventSerializer})
class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        PUT, PATCH, DELETE requests are available only to organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsOrganizerOrAdmin()]


@extend_schema(request=SessionSerializer, responses={200: SessionSerializer})
class SessionListCreateAPIView(ListCreateAPIView):
    """View for listing and creating sessions."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        POST request is available only to organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsOrganizerOrAdmin()]


@extend_schema(responses={200: SessionSerializer})
class SessionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting sessions."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        PUT, PATCH, DELETE requests are available to:
        - Session's speaker (if they're the assigned speaker)
        - Organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]

        # For PUT, PATCH, DELETE: check if user is speaker of this session or organizer/admin
        return [IsSpeakerOrOrganizerOrAdmin()]

    def check_object_permissions(self, request, obj):
        """
        Check if speaker has permission to edit their own session
        """
        super().check_object_permissions(request, obj)

        # If user has organizer or admin role, they're already allowed by the permission class
        if (
            hasattr(request.user, "role")
            and request.user.role
            and request.user.role.display in [UserRoles.ORGANIZER, UserRoles.ADMIN]
        ):
            return

        # If user is the speaker of this session, allow access
        if obj.speaker and obj.speaker.user == request.user:
            return

        # Otherwise, deny access
        self.permission_denied(
            request, message="You don't have permission to edit this session."
        )


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


@extend_schema(responses={200: EventWithGuestSpeakersSerializer})
class EventDetailAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting events with detailed speaker info."""

    queryset = Event.objects.all()
    serializer_class = EventWithGuestSpeakersSerializer
    permission_classes = (AllowAny,)


@api_view(["POST"])
@permission_classes([IsOrganizerOrAdmin])  # Only organizers and admins can add speakers
def add_speaker_to_event(request, event_id):
    """Add a speaker to an event."""
    try:
        event = get_object_or_404(Event, id=event_id)
        speaker_id = request.data.get("speaker_id")

        if not speaker_id:
            return Response(
                {"error": "Speaker ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        speaker = get_object_or_404(SpeakerProfile, id=speaker_id)

        # Add this speaker to the event's speakers
        event.speakers.add(speaker)

        return Response(
            {"message": "Speaker added to event successfully"},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes(
    [IsOrganizerOrAdmin]
)  # Only organizers and admins can remove speakers
def remove_speaker_from_event(request, event_id):
    """Remove a speaker from an event."""
    try:
        event = get_object_or_404(Event, id=event_id)
        speaker_id = request.data.get("speaker_id")

        if not speaker_id:
            return Response(
                {"error": "Speaker ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        speaker = get_object_or_404(SpeakerProfile, id=speaker_id)

        # Remove this speaker from the event's speakers
        event.speakers.remove(speaker)

        return Response(
            {"message": "Speaker removed from event successfully"},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@permission_classes([AllowAny])
def list_event_speakers(request, event_id):
    """List all speakers for an event."""
    try:
        event = get_object_or_404(Event, id=event_id)
        speakers = event.speakers.all()

        serializer = SpeakerProfileSerializer(speakers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@permission_classes([AllowAny])  # Public view - everyone can see sessions
def list_event_sessions(request, event_id):
    """List all sessions for an event with speaker details."""
    try:
        event = get_object_or_404(Event, id=event_id)
        sessions = event.sessions.all()

        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes(
    [IsOrganizerOrAdmin]
)  # Only organizers and admins can create sessions
def create_session_with_speaker(request, event_id):
    """Create a new session with a speaker for an event."""
    try:
        event = get_object_or_404(Event, id=event_id)
        speaker_id = request.data.get("speaker_id")

        if not speaker_id:
            return Response(
                {"error": "Speaker ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        speaker = get_object_or_404(SpeakerProfile, id=speaker_id)

        # Create session data with event and speaker
        session_data = {
            **request.data,
            "event": event.id,
            "speaker": speaker.id,
        }

        serializer = SessionSerializer(data=session_data)
        if serializer.is_valid():
            serializer.save()

            # Also add speaker to event's speakers if not already there
            if speaker not in event.speakers.all():
                event.speakers.add(speaker)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    except SpeakerProfile.DoesNotExist:
        return Response(
            {"error": "Speaker not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
