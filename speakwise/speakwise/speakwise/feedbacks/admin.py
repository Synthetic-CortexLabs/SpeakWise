"""feedback admin."""

from django.contrib import admin
from django.db.models import Avg

from speakwise.feedbacks.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Enhanced feedback admin for better management."""

    list_display = [
        "session",
        "attendee",
        "overall_rating",
        "engagement",
        "clarity",
        "speaker_knowledge",
        "is_anonymous",
        "is_editable",
        "created_at",
    ]
    list_filter = [
        "session",
        "session__event",
        "overall_rating",
        "is_anonymous",
        "is_editable",
        "created_at",
    ]
    search_fields = [
        "session__name",
        "attendee__email",
        "attendee__first_name",
        "attendee__last_name",
        "comment",
    ]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    fieldsets = (
        ("Basic Information", {"fields": ("session", "attendee", "overall_rating")}),
        (
            "Detailed Ratings",
            {
                "fields": (
                    "engagement",
                    "clarity",
                    "content_depth",
                    "speaker_knowledge",
                    "practical_relevance",
                ),
            },
        ),
        (
            "Additional Information",
            {"fields": ("comment", "is_anonymous", "is_editable")},
        ),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )

    def get_queryset(self, request):
        """Optimize queryset with select_related."""
        return super().get_queryset(request).select_related("session", "attendee", "session__event")

    def changelist_view(self, request, extra_context=None):
        """Add summary statistics to the changelist."""
        response = super().changelist_view(request, extra_context=extra_context)

        try:
            qs = response.context_data["cl"].queryset
            summary_stats = qs.aggregate(
                avg_overall=Avg("overall_rating"),
                avg_engagement=Avg("engagement"),
                avg_clarity=Avg("clarity"),
                avg_content_depth=Avg("content_depth"),
                avg_speaker_knowledge=Avg("speaker_knowledge"),
                avg_practical_relevance=Avg("practical_relevance"),
            )

            response.context_data["summary_stats"] = {
                "total_feedback": qs.count(),
                "avg_overall": round(summary_stats["avg_overall"] or 0, 2),
                "avg_engagement": round(summary_stats["avg_engagement"] or 0, 2),
                "avg_clarity": round(summary_stats["avg_clarity"] or 0, 2),
                "avg_content_depth": round(summary_stats["avg_content_depth"] or 0, 2),
                "avg_speaker_knowledge": round(
                    summary_stats["avg_speaker_knowledge"] or 0,
                    2,
                ),
                "avg_practical_relevance": round(
                    summary_stats["avg_practical_relevance"] or 0,
                    2,
                ),
            }
        except (AttributeError, KeyError):
            pass

        return response
