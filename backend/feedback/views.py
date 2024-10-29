"""This module contains the views for the feedback app."""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Feedback
from .serializers import FeedbackSerializer


class ListCreateFeedbackView(ListCreateAPIView):
    """Feedback list and create api endpoint."""

    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer


class RetrieveUpdateDestroyFeedbackView(RetrieveUpdateDestroyAPIView):
    """retrieve, delete and update endpoint for feedback."""

    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
