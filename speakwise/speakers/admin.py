# Register your models here.
from django.contrib import admin

from speakwise.speakers.models import SkillTag
from speakwise.speakers.models import SpeakerProfile
from speakwise.speakers.models import SpeakerSocialLink

admin.site.register(SpeakerProfile)
admin.site.register(SkillTag)
admin.site.register(SpeakerSocialLink)
