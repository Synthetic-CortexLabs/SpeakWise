"""Speakers serializers."""

from rest_framework import serializers
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from speakwise.speakers.models import SkillTag
from speakwise.speakers.models import SpeakerDashboard
from speakwise.speakers.models import (
    SpeakerProfile,  # Updated from Speaker to SpeakerProfile
)
from speakwise.speakers.models import SpeakerSocialLink


class SpeakerSerializer(ModelSerializer):
    """Speaker serializer."""

    class Meta:
        """Meta class."""

        model = SpeakerProfile
        fields = '__all__'
        model = SpeakerProfile
        fields = '__all__'


class SkillTagSerializer(serializers.ModelSerializer):
    """Serializer for the SkillTag model.
    
    Handles serialization of speaker skill tags.
    """
    """Serializer for the SkillTag model.
    
    Handles serialization of speaker skill tags.
    """
    class Meta:
        model = SkillTag
        fields = ["id", "name"]
        fields = ["id", "name"]


class SpeakerSocialLinkSerializer(serializers.ModelSerializer):
    """Serializer for the SpeakerSocialLink model.
    
    Handles serialization of speaker social media links.
    """
    """Serializer for the SpeakerSocialLink model.
    
    Handles serialization of speaker social media links.
    """
    class Meta:
        model = SpeakerSocialLink
        fields = ["id", "social_name", "social_url", "is_active", "display_order"]
        fields = ["id", "social_name", "social_url", "is_active", "display_order"]


class SpeakerProfileSerializer(serializers.ModelSerializer):
    """Serializer for the SpeakerProfile model.
    
    Handles serialization of speaker profile information including nested
    skill tags and social links.

    Attributes:
        skill_tags: Nested SkillTagSerializer (read-only)
        social_links: Nested SpeakerSocialLinkSerializer (read-only)
        full_name: SerializerMethodField for speaker's full name
    """
    """Serializer for the SpeakerProfile model.
    
    Handles serialization of speaker profile information including nested
    skill tags and social links.

    Attributes:
        skill_tags: Nested SkillTagSerializer (read-only)
        social_links: Nested SpeakerSocialLinkSerializer (read-only)
        full_name: SerializerMethodField for speaker's full name
    """
    skill_tags = SkillTagSerializer(many=True, read_only=True)
    social_links = SpeakerSocialLinkSerializer(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = SpeakerProfile
        fields = [
            "id", "speaker_user", "organization", "short_bio", "long_bio",
            "country", "avatar", "skill_tags", "social_links", "full_name"
            "id", "speaker_user", "organization", "short_bio", "long_bio",
            "country", "avatar", "skill_tags", "social_links", "full_name"
        ]

    def get_full_name(self, obj):
        """Returns the speaker's full name from the user model."""

        return obj.speaker_user.get_full_name()


class SpeakerDashboardSerializer(serializers.ModelSerializer):
    """Serializer for the SpeakerDashboard model.
    
    Handles serialization of speaker dashboard data including
    feedback statistics.

    Attributes:
        feedback_stats: SerializerMethodField for computed feedback statistics
    """
    """Serializer for the SpeakerDashboard model.
    
    Handles serialization of speaker dashboard data including
    feedback statistics.

    Attributes:
        feedback_stats: SerializerMethodField for computed feedback statistics
    """
    feedback_stats = serializers.SerializerMethodField()

    class Meta:
        model = SpeakerDashboard
        fields = ["id", "speaker_profile", "feedback_stats"]
        fields = ["id", "speaker_profile", "feedback_stats"]

    def get_feedback_stats(self, obj):
        """Compiles feedback statistics for the speaker.
        
        Returns:
            dict: Contains total events, average rating, and conference-specific ratings
        """
        """Compiles feedback statistics for the speaker.
        
        Returns:
            dict: Contains total events, average rating, and conference-specific ratings
        """
        return {
            "total_events": obj.total_events,
            "average_rating": obj.average_feedback_rating,
            "conference_ratings": obj.feedback_rate_per_conference
            "total_events": obj.total_events,
            "average_rating": obj.average_feedback_rating,
            "conference_ratings": obj.feedback_rate_per_conference
        }
