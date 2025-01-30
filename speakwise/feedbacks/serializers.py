"""feedback serializers."""

from rest_framework.serializers import ModelSerializer
from speakwise.feedbacks.models import Feedback


class FeedbackSerializer(ModelSerializer):
    """Feedback serializer."""

    class Meta:
        """Meta class."""

        model = Feedback
        exclude = ["created_at", "updated_at"]
