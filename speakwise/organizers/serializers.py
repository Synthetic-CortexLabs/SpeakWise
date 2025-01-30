"""organizers serializer file."""

from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from speakwise.organizers.models import Organizers, SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    """social links serializer."""

    class Meta:
        """meta options."""

        model = SocialLinks
        exclude = ["created_at", "updated_at", "organizer"]


class OrganizerSerializer(WritableNestedModelSerializer):
    """organizers serializer."""

    organizers_social_accounts = SocialLinksSerializer(many=True, required=False)

    class Meta:
        """meta options."""

        model = Organizers
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
