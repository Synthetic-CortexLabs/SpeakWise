from django.contrib import admin

from .models import TeamMember
from .models import TeamSocial

# Register your models here.


class TeamSocialInline(admin.TabularInline):
    """Inline admin for TeamSocial model."""

    model = TeamSocial
    extra = 1
    fields = ["social_name", "social_url"]
    verbose_name = "Social Link"
    verbose_name_plural = "Social Links"


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    """Admin configuration for TeamMember model."""

    list_display = [
        "name",
        "role",
        "is_active",
        "display_order",
        "created_at",
        "social_links_count",
    ]
    list_filter = ["is_active", "created_at"]
    search_fields = ["name", "role", "short_bio"]
    list_editable = ["is_active", "display_order"]
    ordering = ["display_order", "name"]
    inlines = [TeamSocialInline]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": ("name", "role", "short_bio", "avatar"),
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
    
    def social_links_count(self, obj):
        """Display count of social links for each team member."""
        return obj.social_links.count()
    social_links_count.short_description = "Social Links"


@admin.register(TeamSocial)
class TeamSocialAdmin(admin.ModelAdmin):
    """Admin configuration for TeamSocial model."""
    
    list_display = [
        "team",
        "social_name",
        "social_url",
        "created_at",
    ]
    list_filter = ["social_name", "created_at"]
    search_fields = ["team__name", "social_name", "social_url"]
    ordering = ["team__name", "social_name"]
    
    fieldsets = (
        (
            "Social Link Information",
            {
                "fields": ("team", "social_name", "social_url"),
            },
        ),
    )
