"""organizers serializer file."""

from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from speakwise.organizers.models import (
    AttendanceEmails,
    Organizers,
    OrganizersSocialLinks,
)


class OrganizersSocialLinksSerializer(serializers.ModelSerializer):
    """social links serializer."""

    class Meta:
        """meta options."""

        model = OrganizersSocialLinks
        exclude = ["created_at", "updated_at", "organizer"]


class OrganizerSerializer(WritableNestedModelSerializer):
    """organizers serializer."""

    organizers_social_accounts = OrganizersSocialLinksSerializer(
        many=True, required=False
    )

    class Meta:
        """meta options."""

        model = Organizers
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]


class AttendanceSerializer(serializers.ModelSerializer):
    """file upload serializer."""

    class Meta:
        """meta options."""

        model = AttendanceEmails
        fields = ["email"]
