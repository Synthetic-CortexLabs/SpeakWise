"""users serializers."""

from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from speakwise.users.models import User
from speakwise.users.models import UserRole
from rest_framework import serializers

from speakwise.users.models import User
from speakwise.users.models import UserRole


class UserRoleSerializer(serializers.ModelSerializer):
    """User role serializer."""

    class Meta:
        """Meta class."""

        model = UserRole
        fields = ["id", "role"]


class UserSerializer(WritableNestedModelSerializer):
    """User serializer."""

    role = UserRoleSerializer(required=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "password"]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        role_data = validated_data.pop("role", None)
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        if role_data:
            UserRole.objects.create(user=user, **role_data)
        user.set_password(password)
        user.save()
        return user
