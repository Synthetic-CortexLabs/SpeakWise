"""Feedback serializers."""

from rest_framework.serializers import ModelSerializer
from .models import Feedback, FeedbackTrend


class FeedbackSerializer(ModelSerializer):
    """Feedback serializer."""

    class Meta:
        """Meta class."""

        model = Feedback
        fields = "__all__"


class FeedbackTrendSerializer(ModelSerializer):
    """Feedback trend serializer."""

    class Meta:
        """Meta class."""

        model = FeedbackTrend
        fields = ["__all__"]
