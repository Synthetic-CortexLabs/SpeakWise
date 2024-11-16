from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from speakwise.users.models import User, UserRole


class UserRoleSerializer(serializers.Serializer):
    """User role serializer."""

    class Meta:
        model = UserRole
        fields = ["id", "display"]


class UserSerializer(WritableNestedModelSerializer):
    """User serializer."""

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

        extra_kwargs = {"password": {"write_only": True}}
