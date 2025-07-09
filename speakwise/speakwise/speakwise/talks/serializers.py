"""Talks serializers module."""

from rest_framework import serializers

from speakwise.talks.models import Talks


class TalkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Talks model.
    Converts Talks model instances to and from JSON format.
    """

    class Meta:
        model = Talks
        exclude = ["created_at", "updated_at"]


