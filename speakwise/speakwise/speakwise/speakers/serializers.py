"""Speakers serializers."""

from rest_framework.serializers import ModelSerializer

from speakwise.attendees import serializers
from speakwise.speakers.models import Handles

from .models import Speaker


class SpeakerSerializer(ModelSerializer):
    """Speaker serializer."""

    class Meta:
        """Meta class."""

        model = Speaker
        exclude = ["created_at", "updated_at"]


class HanndlesSerializer(serializers.ModelSerializer):
    """social links serializer."""

    class Meta:
        """meta options."""

        model = Handles
        exclude = ["created_at", "updated_at", "speaker"]


