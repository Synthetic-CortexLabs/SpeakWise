# Register your models here.
from django.contrib import admin

from speakwise.speakers.models import SkillTag
from speakwise.speakers.models import SpeakerProfile
from speakwise.speakers.models import SpeakerSocialLink


@admin.register(SkillTag)
class SkillTagAdmin(admin.ModelAdmin):
    """Admin view for the SkillTag model."""

    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(SpeakerProfile)
class SpeakerProfileAdmin(admin.ModelAdmin):
    """Admin view for the SpeakerProfile model."""

    list_display = ("speaker_user",)
    search_fields = ("user__username", "bio", "location")
    list_filter = ("speaker_user",)
    ordering = ("-created_at",)


@admin.register(SpeakerSocialLink)
class SpeakerSocialLinkAdmin(admin.ModelAdmin):
    """Admin view for the SpeakerSocialLink model."""

    list_display = ("speaker", "social_name", "social_url")
    search_fields = ("speaker__user__username", "social_name", "social_url")
    list_filter = ("speaker",)
    ordering = ("-created_at",)
