"""Speakers serializers."""

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import SkillTag
from .models import Speaker
from .models import SpeakerDashboard
from .models import SpeakerProfile
from .models import SpeakerSocialLink


class SpeakerSerializer(ModelSerializer):
    """Speaker serializer."""

    class Meta:
        """Meta class."""

        model = Speaker
        exclude = ["created_at", "updated_at"]


class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = ["id", "name"]


class SpeakerSocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerSocialLink
        fields = ["id", "social_name", "social_url", "is_active", "display_order"]


class SpeakerProfileSerializer(serializers.ModelSerializer):
    skill_tags = SkillTagSerializer(many=True, read_only=True)
    social_links = SpeakerSocialLinkSerializer(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = SpeakerProfile
        fields = [
            "id", "speaker_user", "organization", "short_bio", "long_bio",
            "country", "avatar", "skill_tags", "social_links", "full_name"
        ]

    def get_full_name(self, obj):
        return obj.speaker_user.get_full_name()


class SpeakerDashboardSerializer(serializers.ModelSerializer):
    feedback_stats = serializers.SerializerMethodField()

    class Meta:
        model = SpeakerDashboard
        fields = ["id", "speaker_profile", "feedback_stats"]

    def get_feedback_stats(self, obj):
        return {
            "total_events": obj.total_events,
            "average_rating": obj.average_feedback_rating,
            "conference_ratings": obj.feedback_rate_per_conference
        }
