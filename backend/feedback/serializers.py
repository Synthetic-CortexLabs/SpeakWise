from rest_framework.serializers import ModelSerializer
from .models import Feedback, FeedbackTrend


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["__all__"]


class FeedbackTrendSerializer(ModelSerializer):
    class Meta:
        model = FeedbackTrend
        fields = ["__all__"]
