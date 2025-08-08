# Register your models here.
from django.contrib import admin
from speakwise.organizers.models import (
    Organizers,
    SocialLinks,
    AttendanceEmails,
    AttendeeCSVUpload,
)



class OrganizerAdmin(admin.ModelAdmin):
    """Admin view for the Organizers model."""

    list_display = ("events", "organization")
    search_fields = ("events", "organization")
    list_filter = ("events", "organization")
    ordering = ("-created_at",)


class SocialLinksAdmin(admin.ModelAdmin):
    """Admin view for the SocialLinks model."""

    list_display = ("social_name", "social_link")
    search_fields = ("social_name", "social_link")
    list_filter = ("social_name",)
    ordering = ("-created_at",)


class AttendanceEmailsAdmin(admin.ModelAdmin):
    """Admin view for the AttendanceEmails model."""

    list_display = ("email", "event")
    search_fields = ("email", "event")
    list_filter = ("event",)
    ordering = ("-created_at",)


class AttendeeCSVUploadAdmin(admin.ModelAdmin):
    """Admin view for the AttendeeCSVUpload model."""

    list_display = [
        "event",
        "organizer",
        "uploaded_at",
        "processed",
        "success_count",
        "error_count",
    ]
    list_filter = ["processed", "uploaded_at", "event"]
    search_fields = ["event__title", "organizer__email"]
    readonly_fields = [
        "uploaded_at",
        "processed_at",
        "success_count",
        "error_count",
        "error_log",
    ]

    actions = ["process_csv_files"]

    def process_csv_files(self, request, queryset):
        """Admin action to process selected CSV files."""
        processed_count = 0
        for upload in queryset.filter(processed=False):
            success_count, errors = upload.process_csv()
            processed_count += 1

        self.message_user(request, f"Processed {processed_count} CSV files.")

    process_csv_files.short_description = "Process selected CSV files"

    def save_model(self, request, obj, form, change):
        """Auto-process CSV after upload if not processed yet."""
        super().save_model(request, obj, form, change)
        if not obj.processed:
            try:
                success_count, errors = obj.process_csv()
                msg = f"CSV processed successfully. {success_count} attendees created."
                if errors:
                    msg += f" {len(errors)} errors occurred."
                self.message_user(request, msg)
            except Exception as e:
                self.message_user(
                    request, f"Error processing CSV: {str(e)}", level="ERROR"
                )


admin.site.register(Organizers, OrganizerAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)
admin.site.register(AttendanceEmails, AttendanceEmailsAdmin)
admin.site.register(AttendeeCSVUpload, AttendeeCSVUploadAdmin)
