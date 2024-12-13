from django.contrib import admin

from speakwise.events.models import Country
from speakwise.events.models import Event
from speakwise.events.models import Region
from speakwise.events.models import Session

# Register your models here.

admin.site.register(Event)
admin.site.register(Session)
admin.site.register(Country)
admin.site.register(Region)
