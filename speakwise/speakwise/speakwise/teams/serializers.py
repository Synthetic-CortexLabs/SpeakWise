"""team serializers."""

from speakwise.teams.models import TeamMember, TeamSocial
from rest_framework import serializers


class TeamSocialSerializer(serializers.ModelSerializer):
    """Serializer for the TeamSocial model."""

    class Meta:
        model = TeamSocial
        exclude = ["created_at", "updated_at", "team"]


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer for the TeamMember model."""

    avatar_url = serializers.SerializerMethodField()
    social_links = TeamSocialSerializer(many=True, required=False)

    class Meta:
        model = TeamMember
        exclude = ["created_at", "updated_at"]

    def get_avatar_url(self, obj):
        """Get the full URL for the avatar image."""
        if obj.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None
