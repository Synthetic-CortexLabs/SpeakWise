"""Serializers for the events app."""

import base64

from django.core.files.base import ContentFile
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

    event_image = serializers.ImageField(required=False, allow_null=True)

    country = CountrySerializer(required=False, many=True)

    class Meta:
        """Meta class for the EventSerializer."""

        model = Event
        fields = "__all__"

        # decodein theimage
        def to_internal_value(self, data):
            if data.get("event_image"):
                # Handle base64 image
                if ";base64," in data["event_image"]:
                    format, imgstr = data["event_image"].split(";base64,")  # noqa: A001
                    ext = format.split("/")[-1]
                    data["event_image"] = ContentFile(
                        base64.b64decode(imgstr),
                        name=f"temp.{ext}",
                    )
            return super().to_internal_value(data)


class SessionSerializer(serializers.ModelSerializer):
    """Serializer for the Session model."""

    class Meta:
        """Meta class for the SessionSerializer."""

        model = Session
        exclude = ("created_at", "updated_at")
