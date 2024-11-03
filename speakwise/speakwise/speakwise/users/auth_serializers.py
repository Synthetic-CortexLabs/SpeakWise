from rest_framework import serializers
from organizers.models import Organizer
from speakers.models import Speaker

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    ACCOUNT_TYPES = [
        ("speaker", "speaker"),
        ("attendee", "attendee"),
        ("organizer", "organizer")
    ]

    ACCOUNT_TYPE_MODEL_MAP = {
        "organizer": Organizer,
        "speaker": Speaker
        # "attendee" is omitted if no additional model needs to be created
    }
    
    account_type = serializers.ChoiceField(choices=ACCOUNT_TYPES)
    class Meta:
        model = User
        fields = ["email","password","role"]

    def create(self, validated_data):
        role = validated_data.pop("role")
        user = super().create(validated_data)

        # Dynamically get model from account type
        model = self.ACCOUNT_TYPE_MODEL_MAP.get(role)
        if model:
            model.objects.create(user=user)

        return user
