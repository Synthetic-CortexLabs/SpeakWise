# Register your models here.
from django.contrib import admin

from speakwise.events.models import Country
from speakwise.events.models import Event
from speakwise.events.models import Region
from speakwise.events.models import Session

admin.site.register(Country)


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "event_nickname",
        "location",
        "start_date_time",
        "end_date_time",
        "is_active",
    )
    search_fields = ("title", "event_nickname", "location")
    list_filter = ("is_active",)
    date_hierarchy = "start_date_time"
    ordering = ("start_date_time",)


admin.site.register(Event, EventAdmin)
admin.site.register(Region)
admin.site.register(Session)
