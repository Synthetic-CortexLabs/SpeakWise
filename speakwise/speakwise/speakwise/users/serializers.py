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

            Attendee.objects.create(user=user)
        # (You can add similar logic for Speaker/Organizer if needed)

        return user
