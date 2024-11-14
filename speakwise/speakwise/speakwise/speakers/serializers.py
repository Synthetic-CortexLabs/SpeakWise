"""Speakers serializers."""

from rest_framework.serializers import ModelSerializer

from .models import Speaker


class SpeakerSerializer(ModelSerializer):
    """Speaker serializer."""

    class Meta:
        """Meta class."""

        model = Speaker
        exclude = ["created_at", "updated_at"]
