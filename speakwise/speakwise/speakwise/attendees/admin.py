"""attendees admin."""

from django.contrib import admin

from speakwise.attendees.models import AttendanceCode
from speakwise.attendees.models import Attendee


@admin.register(AttendanceCode)
class AttendanceCodeAdmin(admin.ModelAdmin):
    """AttendanceCode admin."""

    list_display = ("id", "code", "attendee", "created_at")
    search_fields = ("code",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    """Attendee admin."""

    list_display = ("id", "email", "first_name", "last_name", "is_verified")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_verified",)
    ordering = ("-created_at",)
