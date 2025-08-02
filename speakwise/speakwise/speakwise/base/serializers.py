"""Team serializers for the SpeakWise application."""

from rest_framework import serializers

from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer for the TeamMember model."""

    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = [
            "id",
            "name",
            "role",
            "short_bio",
            "avatar",
            "avatar_url",
            "twitter_url",
            "linkedin_url",
            "github_url",
            "website_url",
            "display_order",
        ]

    def get_avatar_url(self, obj):
        """Get the full URL for the avatar image."""
        if obj.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None
