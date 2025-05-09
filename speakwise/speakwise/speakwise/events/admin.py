# Register your models here.
from django.contrib import admin

from speakwise.events.models import Country, Session, Event,Region

class CountryAdmin(admin.ModelAdmin):
    """Country admin."""

    list_display = ("id", "name")
    search_fields = ("name")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

class RegionAdmin(admin.ModelAdmin):
    """Region admin."""

    list_display = ("id", "name", "country")
    search_fields = ("name", "country__name")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

class EventAdmin(admin.ModelAdmin):
    """Event admin."""

    list_display = ("id", "title", "description", "location", "is_active")
    search_fields = ("title", "description", "location")
    list_filter = ("is_active",)
    ordering = ("-created_at",)


class SessionAdmin(admin.ModelAdmin):
    """Session admin."""

    list_display = ("id", "name", "description", "event", "location")
    search_fields = ("title", "event__title")
    list_filter = ("event__is_active",)
    ordering = ("-created_at",)
