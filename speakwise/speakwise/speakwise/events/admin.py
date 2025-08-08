"""events admin."""

# Register your models here.
from django.contrib import admin

from speakwise.events.models import Country, Event, Location, Session, Tag


class CountryAdmin(admin.ModelAdmin):
    """Country admin."""

    list_display = ("id", "name", "code")
    search_fields = ("name", "code")
    list_filter = ("created_at", "code")
    ordering = ("-created_at",)


class LocationAdmin(admin.ModelAdmin):
    """Region admin."""

    list_display = ("id", "venue")
    search_fields = ("venue",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


class EventAdmin(admin.ModelAdmin):
    """Event admin."""

    list_display = (
        "id",
        "title",
        "description",
        "location",
        "start_date_time",
        "end_date_time",
        "is_active",
        "get_tags",
    )
    search_fields = ("title", "description", "location", "tags__name")
    list_filter = ("is_active", "start_date_time", "created_at", "tags")
    ordering = ("-created_at",)
    date_hierarchy = "start_date_time"
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("tags",)  # Better UI for managing many-to-many relationships

    def get_tags(self, obj):
        """Return a comma-separated list of tags."""
        return ", ".join([tag.name for tag in obj.tags.all()])

    get_tags.short_description = "Tags"


class SessionAdmin(admin.ModelAdmin):
    """Session admin."""

    list_display = ("id", "name", "description", "event", "location")
    search_fields = ("name", "event__title")
    list_filter = ("event__is_active",)
    ordering = ("-created_at",)


class TagAdmin(admin.ModelAdmin):
    """Tag admin."""

    list_display = ("id", "name", "color")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("name",)


# Register models with admin
admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Tag, TagAdmin)
