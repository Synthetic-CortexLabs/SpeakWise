"""users serializers."""

from rest_framework import serializers
from speakwise.users.models import User, UserRole
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserRoleSerializer(serializers.ModelSerializer):
    """User role serializer."""

    class Meta:
        """Meta class."""

        model = UserRole
        fields = ["id", "role"]


class UserSerializer(WritableNestedModelSerializer):
    """User serializer."""

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

        extra_kwargs = {"password": {"write_only": True}}
