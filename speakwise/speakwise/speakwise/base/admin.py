"""Team admin configuration for the SpeakWise application."""

from django.contrib import admin

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    """Admin configuration for TeamMember model."""

    list_display = [
        "name",
        "role",
        "is_active",
        "display_order",
        "created_at",
    ]
    list_filter = ["is_active", "created_at"]
    search_fields = ["name", "role", "short_bio"]
    list_editable = ["is_active", "display_order"]
    ordering = ["display_order", "name"]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": ("name", "role", "short_bio", "avatar"),
            },
        ),
        (
            "Social Media Links",
            {
                "fields": (
                    "twitter_url",
                    "linkedin_url",
                    "github_url",
                    "website_url",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Display Settings",
            {
                "fields": ("is_active", "display_order"),
            },
        ),
    )

    def get_queryset(self, request):
        """Override queryset to show all team members."""
        return super().get_queryset(request)
