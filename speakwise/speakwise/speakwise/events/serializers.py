"""Serializers for the events app."""

import base64

from django.core.files.base import ContentFile
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from speakwise.events.models import Event, Location, Country, Session, Tag


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for the Country model."""

    class Meta:
        """Meta class for the CountrySerializer."""

        model = Country
        exclude = ("created_at", "updated_at")



class LocationSerializer(WritableNestedModelSerializer):
    """Serializer for the Region model."""

    country = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        """Meta class for the RegionSerializer."""

        model = Location
        exclude = ("created_at", "updated_at")


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the Tag model."""

    class Meta:
        """Meta class for the TagSerializer."""

        model = Tag
        fields = ("id", "name", "color")



class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model."""

    event_image = serializers.ImageField(required=False, allow_null=True)
    tags = TagSerializer(many=True, read_only=True)
    website = serializers.URLField(required=False, allow_blank=True)
    short_description = serializers.CharField(required=False, allow_blank=True)
    location = LocationSerializer(required=False)
    # Frontend-specific computed fields
    name = serializers.CharField(source="title", read_only=True)
    date = serializers.SerializerMethodField()
    date_range = serializers.SerializerMethodField()  # New field for start/end dates
    attendees = serializers.SerializerMethodField()
    speakers = serializers.SerializerMethodField()

    class Meta:
        """Meta class for the EventSerializer."""

        model = Event
        fields = "__all__"

    def get_date(self, obj):
        """Format date range for frontend display - keeping for backward compatibility."""
        if obj.start_date_time and obj.end_date_time:
            start_date = obj.start_date_time.strftime("%B %d")
            end_date = obj.end_date_time.strftime("%d, %Y")

            # Check if same month/year
            if (
                obj.start_date_time.month == obj.end_date_time.month
                and obj.start_date_time.year == obj.end_date_time.year
            ):
                if obj.start_date_time.day == obj.end_date_time.day:
                    # Same day
                    return obj.start_date_time.strftime("%B %d, %Y")
                # Same month, different days
                return f"{start_date}-{end_date}"
            # Different months/years
            start_full = obj.start_date_time.strftime("%B %d, %Y")
            end_full = obj.end_date_time.strftime("%B %d, %Y")
            return f"{start_full} - {end_full}"
        return None

    def get_date_range(self, obj):
        """Get separate start and end dates for better display control."""
        if not obj.start_date_time or not obj.end_date_time:
            return {"start": None, "end": None, "same_day": False}

        start_date = obj.start_date_time.strftime("%B %d, %Y")
        start_time = obj.start_date_time.strftime("%I:%M %p")
        end_date = obj.end_date_time.strftime("%B %d, %Y")
        end_time = obj.end_date_time.strftime("%I:%M %p")

        same_day = (
            obj.start_date_time.year == obj.end_date_time.year
            and obj.start_date_time.month == obj.end_date_time.month
            and obj.start_date_time.day == obj.end_date_time.day
        )

        return {
            "start": {
                "date": start_date,
                "time": start_time,
                "datetime": obj.start_date_time.isoformat(),
            },
            "end": {
                "date": end_date,
                "time": end_time,
                "datetime": obj.end_date_time.isoformat(),
            },
            "same_day": same_day,
        }

    def to_internal_value(self, data):
        """Handle base64 image encoding."""
        if data.get("event_image"):
            # Handle base64 image
            if ";base64," in data["event_image"]:
                img_format, imgstr = data["event_image"].split(";base64,")
                ext = img_format.split("/")[-1]
                data["event_image"] = ContentFile(
                    base64.b64decode(imgstr),
                    name=f"temp.{ext}",
                )
        return super().to_internal_value(data)


class SessionSerializer(serializers.ModelSerializer):
    """Serializer for the Session model."""

    speaker_details = serializers.SerializerMethodField()

    class Meta:
        """Meta class for the SessionSerializer."""

        model = Session
        exclude = ("created_at", "updated_at")

    def get_speaker_details(self, obj):
        """Get detailed information about the session's speaker."""
        if obj.speaker:
            from speakwise.speakers.serializers import SpeakerProfileSerializer

            return SpeakerProfileSerializer(obj.speaker).data
        return None
