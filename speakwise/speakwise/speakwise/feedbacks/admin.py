"""feedback admin."""
from django.contrib import admin
from speakwise.feedbacks.models import Feedback


class AdminFeedback(admin.ModelAdmin):
    """feedback admin."""

    list_display = ["session", "attendee"]
    list_filter = ["session"]
    search_fields = ["session"]
    ordering = ("-created_at",)

admin.site.register(Feedback, AdminFeedback)
