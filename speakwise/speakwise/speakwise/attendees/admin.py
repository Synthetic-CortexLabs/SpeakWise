"""attendees admin."""

from django.contrib import admin
from speakwise.attendees.models import AttendanceCode, Attendee


class AttendanceCodeAdmin(admin.ModelAdmin):
    """AttendanceCode admin."""

    list_display = ("id", "code", "attendee", "created_at")
    search_fields = ("code",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


class AttendeeAdmin(admin.ModelAdmin):
    """Attendee admin."""

    list_display = ("id", "email", "first_name", "last_name", "is_verified")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_verified",)
    ordering = ("-created_at",)


admin.site.register(AttendanceCode, AttendanceCodeAdmin)
admin.site.register(Attendee, AttendeeAdmin)
