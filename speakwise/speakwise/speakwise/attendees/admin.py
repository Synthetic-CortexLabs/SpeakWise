"""attendees admin."""
from django.contrib import admin

from speakwise.attendees.models import AttendanceCode
from speakwise.attendees.models import Attendee

# Register your models here.
admin.site.register(Attendee)
admin.site.register(AttendanceCode)

