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
        fields = ["id", "first_name", "last_name", "email", "role"]
        read_only_fields = ["id", "role"]
