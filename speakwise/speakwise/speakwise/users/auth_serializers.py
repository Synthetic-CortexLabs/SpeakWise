from rest_framework import serializers
from speakers.serializers import SpeakerSerializer
from organizers.serializers import OrganizerSerializer
from organizers.models import Organizer
from speakers.models import Speaker
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    speaker_profile = SpeakerSerializer(required=False)
    organizer_profile = OrganizerSerializer(required=False)
    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'role', 'speaker_profile', 'organizer_profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        speaker_profile_data = validated_data.pop('speaker_profile', None)
        organizer_profile_data = validated_data.pop('organizer_profile', None)
        
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        if  user.role == 'SPEAKER' and speaker_profile_data:
            Speaker.objects.create(user=user, **speaker_profile_data)
        elif user.role == 'ORGANIZER' and organizer_profile_data:
            Organizer.objects.create(user=user, **organizer_profile_data)

        return user

    def validate(self, data):
        role = data.get('role')
        speaker_profile = data.get('speaker_profile')
        organizer_profile = data.get('organizer_profile')
        if role == 'SPEAKER' and not speaker_profile:
            raise serializers.ValidationError(
                {"speaker_profile": "Speaker profile data is required for speaker role"}
            )
        elif role == 'ORGANIZER' and not organizer_profile:
            raise serializers.ValidationError(
                {"organizer_profile": "Organizer profile data is required for organizer role"}
            )

        return data