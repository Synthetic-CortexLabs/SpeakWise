"""Extended event serializers with more detailed speaker and session information."""

from rest_framework import serializers
from .serializers import EventSerializer, SessionSerializer
from speakwise.speakers.serializers import SpeakerProfileSerializer


class EventWithGuestSpeakersSerializer(EventSerializer):
    """Extended Event serializer that includes full speaker profile data."""

    speaker_profiles = serializers.SerializerMethodField()
    event_sessions = serializers.SerializerMethodField()

    def get_speaker_profiles(self, obj):
        """Get detailed speaker profiles for this event."""
        speakers = obj.speakers.all()
        return SpeakerProfileSerializer(speakers, many=True).data

    def get_event_sessions(self, obj):
        """Get sessions for this event with speaker details."""
        sessions = obj.sessions.all()
        return SessionSerializer(sessions, many=True).data
