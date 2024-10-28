from rest_framework import serializers
from .models import Event


class EventsSerializer(serializers.ModelSerializer):
    """Events serializer."""

    class Meta:
        """Meta class."""

        model = Event
        fields = "__all__"
