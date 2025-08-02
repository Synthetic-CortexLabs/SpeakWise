"""users serializers."""

from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from speakwise.users.models import User
from speakwise.users.models import UserRole


class UserRoleSerializer(serializers.ModelSerializer):
    """User role serializer."""

    class Meta:
        """Meta class."""

        model = UserRole
        fields = ["id", "display"]


class UserSerializer(WritableNestedModelSerializer):
    """User serializer."""

    role = UserRoleSerializer(required=False)

    class Meta:
        """Meta class."""

        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "nationality",
            "role",
            "password",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Create a new user."""
        role_data = validated_data.pop("role", None)
        password = validated_data.pop("password")
        # Look up the UserRole by display value and assign to user
        if role_data and "display" in role_data:
            from speakwise.users.models import UserRole

            role_obj = UserRole.objects.get(display=role_data["display"])
            validated_data["role"] = role_obj
        user = User.objects.create_user(password=password, **validated_data)

        # Create Attendee profile if role is attendee
        if role_data and role_data.get("display") == "attendee":
            from speakwise.attendees.models import Attendee

            # Create or get attendee with the user's email
            attendee, created = Attendee.objects.get_or_create(
                email=user.email,
                defaults={
                    "user": user,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            )
            if not created:
                # If attendee already exists, just associate it with the user
                attendee.user = user
                attendee.save()
        
        # Create SpeakerProfile if role is speaker
        elif role_data and role_data.get("display") == "speaker":
            from speakwise.speakers.models import SpeakerProfile

            # Create speaker profile for the user
            SpeakerProfile.objects.create(
                speaker_user=user,
                long_bio="",  # Required field, set to empty initially
            )
        
        # Create OrganizerProfile if role is organizer
        elif role_data and role_data.get("display") == "organizer":
            from speakwise.organizers.models import Organizers

            # Create organizer profile for the user
            Organizers.objects.create(
                user_id=user,
                organization="",  # Required field, set to empty initially
            )

        return user
