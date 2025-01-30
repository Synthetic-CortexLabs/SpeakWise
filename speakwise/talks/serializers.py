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
        fields = [
            "id",
            "event_id",
            "title",
            "description",
            "start_time",
            "end_time",
            "speaker_id",
        ]
