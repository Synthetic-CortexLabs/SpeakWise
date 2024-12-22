"""attendees serializers."""

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.serializers import ModelSerializer

from speakwise.attendees.models import AttendanceCode
from speakwise.attendees.models import Attendee


class AttendanceCodeSerializer(ModelSerializer):
    """attendance code serializer."""

    class Meta:
        """meta options."""

        model = AttendanceCode
        exclude = ["created_at", "updated_at", "attendee"]


class AttendeeSerializer(WritableNestedModelSerializer):
    """attendees serializer class."""

    attendee_unique_code = AttendanceCodeSerializer(required=False)

    class Meta:
        """meta options."""

        model = Attendee
        exclude = ["created_at", "updated_at"]
