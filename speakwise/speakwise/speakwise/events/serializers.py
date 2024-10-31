"""Serializers for the events app."""

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Country
from .models import Event
from .models import Region
from .models import Session


class RegionSerializer(serializers.ModelSerializer):
    """Serializer for the Region model."""

    class Meta:
        """Meta class for the RegionSerializer."""

        model = Region
        exclude = ("created_at", "updated_at", "country")


class CountrySerializer(WritableNestedModelSerializer):
    """Serializer for the Country model."""

    region = RegionSerializer(required=False, many=True)

    class Meta:
        """Meta class for the CountrySerializer."""

        model = Country
        exclude = ("created_at", "updated_at", "event")


class EventSerializer(WritableNestedModelSerializer):
    """Serializer for the Event model."""

    country = CountrySerializer(required=False, many=True)

    class Meta:
        """Meta class for the EventSerializer."""

        model = Event
        exclude = ("created_at", "updated_at")


class SessionSerializer(serializers.ModelSerializer):
    """Serializer for the Session model."""

    class Meta:
        """Meta class for the SessionSerializer."""

        model = Session
        exclude = ("created_at", "updated_at")
