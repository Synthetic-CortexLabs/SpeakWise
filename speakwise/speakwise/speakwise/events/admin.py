# Register your models here.
from django.contrib import admin

from speakwise.events.models import Country
from speakwise.events.models import Event
from speakwise.events.models import Region
from speakwise.events.models import Session

admin.site.register(Country)
admin.site.register(Event)
admin.site.register(Region)
admin.site.register(Session)
