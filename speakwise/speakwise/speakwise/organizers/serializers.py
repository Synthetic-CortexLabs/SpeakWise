from rest_framework import serializers

from speakwise.organizers.models import Organizer


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ["id", "user_id", "socials", "events", "organization", "avatar"]
        read_only_fields = ["id"]
