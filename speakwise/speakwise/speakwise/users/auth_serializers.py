from organizers.models import Organizer
from organizers.serializers import OrganizerSerializer
from rest_framework import serializers
from speakers.models import Speaker
from speakers.serializers import SpeakerSerializer

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    UserRegistrationSerializer is a ModelSerializer for handling user registration with different roles.
    Attributes:
        speaker_profile (SpeakerSerializer): Optional serializer for speaker profile data.
        organizer_profile (OrganizerSerializer): Optional serializer for organizer profile data.
        role (serializers.CharField): Role of the user, write-only field.
    Meta:
        model (User): The User model associated with this serializer.
        fields (tuple): Fields to be included in the serialized output.
        extra_kwargs (dict): Additional keyword arguments for fields.
    Methods:
        create(validated_data):
            Creates a new User instance along with associated Speaker or Organizer profile based on the role.
            Args:
                validated_data (dict): Validated data for creating the user and profiles.
            Returns:
                User: The created User instance.
        validate(data):
            Validates the input data to ensure that the appropriate profile data is provided based on the role.
            Args:
                data (dict): Input data to be validated.
            Returns:
                dict: Validated data.
            Raises:
                serializers.ValidationError: If the required profile data is not provided for the specified role.
    """

    speaker_profile = SpeakerSerializer(required=False)
    organizer_profile = OrganizerSerializer(required=False)
    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "role",
            "speaker_profile",
            "organizer_profile",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        speaker_profile_data = validated_data.pop("speaker_profile", None)
        organizer_profile_data = validated_data.pop("organizer_profile", None)

        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        if user.role == "SPEAKER" and speaker_profile_data:
            Speaker.objects.create(user=user, **speaker_profile_data)
        elif user.role == "ORGANIZER" and organizer_profile_data:
            Organizer.objects.create(user=user, **organizer_profile_data)

        return user

    def validate(self, data):
        role = data.get("role")
        speaker_profile = data.get("speaker_profile")
        organizer_profile = data.get("organizer_profile")
        if role == "SPEAKER" and not speaker_profile:
            raise serializers.ValidationError(
                {
                    "speaker_profile": "Speaker profile data is required for speaker role"
                },
            )
        if role == "ORGANIZER" and not organizer_profile:
            raise serializers.ValidationError(
                {
                    "organizer_profile": "Organizer profile data is required for organizer role"
                },
            )

        return data
