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
    """user serializer."""

    role = UserRoleSerializer(required=False)

    class Meta:
        """Meta class."""

        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "role",
            "nationality",
            "password",
        ]
        read_only_fields = ["id", "role", "password"]

    def create(self, validated_data):
        """Create a user."""
        role = validated_data.pop("role", None)
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if role:
            user.role = UserRole.objects.get_or_create(**role)[0]
        if password:
            user.set_password(password)
        user.save()
        return user
