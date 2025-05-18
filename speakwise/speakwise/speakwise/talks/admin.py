# Register your models here.
from django.contrib import admin
from speakwise.talks.models import Talks


class TalksAdmin(admin.ModelAdmin):
    """Admin view for the Talks model."""
    list_display = ("event_id", "title","start_time", "end_time")
    search_fields = ('title', 'event_id__title')
    list_filter = ('event_id',)
    ordering = ("-created_at",)


admin.site.register(Talks, TalksAdmin)
