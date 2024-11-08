"""Speakers serializers."""

from rest_framework.serializers import ModelSerializer

from speakwise.base.validators import validate_date_time_values

from .models import Speaker


class SpeakerSerializer(ModelSerializer):
    """Speaker serializer."""

    class Meta:
        """Meta class."""

        model = Speaker
        exclude = ["created_at", "updated_at"]

    def validate(self, data):
        validate_date_time_values(
            data.get("start_date_time"),
            data.get("end_date_time"),
        )
        return data
