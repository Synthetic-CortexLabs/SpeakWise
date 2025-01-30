"""feedback views."""

from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from speakwise.feedbacks.models import Feedback
from speakwise.feedbacks.serializers import FeedbackSerializer


@extend_schema(request=FeedbackSerializer, responses=FeedbackSerializer(many=True))
class FeedbackListCreateView(ListCreateAPIView):
    """Feedback list and create api endpoint."""

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [AllowAny]


@extend_schema(request=FeedbackSerializer, responses=FeedbackSerializer(many=True))
class FeedbackDetailView(RetrieveUpdateDestroyAPIView):
    """retrieve, delete and update endpoint for feedbacks."""

    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]


