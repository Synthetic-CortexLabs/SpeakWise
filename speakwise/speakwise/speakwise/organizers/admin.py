# Register your models here.
from django.contrib import admin
from speakwise.organizers.models import Organizers, SocialLinks, AttendanceEmails

class OrganizerAdmin(admin.ModelAdmin):
    """Admin view for the Organizers model."""
    list_display = ("events", "organization")
    search_fields = ('events', 'organization')
    list_filter = ('events',"organization")
    ordering = ("-created_at",)


class SocialLinksAdmin(admin.ModelAdmin):
    """Admin view for the SocialLinks model."""
    list_display = ("social_name", "social_link")
    search_fields = ('social_name', 'social_link')
    list_filter = ('social_name',)
    ordering = ("-created_at",)

class AttendanceEmailsAdmin(admin.ModelAdmin):
    """Admin view for the AttendanceEmails model."""
    list_display = ("email", "event")
    search_fields = ("email", "event")
    list_filter = ('event',)
    ordering = ("-created_at",)


admin.site.register(Organizers, OrganizerAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)
admin.site.register(AttendanceEmails, AttendanceEmailsAdmin)


