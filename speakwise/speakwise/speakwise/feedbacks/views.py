"""feedback views."""

from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from speakwise.feedbacks.models import Feedback
from speakwise.feedbacks.serializers import FeedbackSerializer
from speakwise.authentication.permissions import (
    IsAttendee,
    IsSpeakerOrOrganizerOrAdmin,
)


@extend_schema(request=FeedbackSerializer, responses=FeedbackSerializer(many=True))
class FeedbackListCreateView(ListCreateAPIView):
    """Feedback list and create api endpoint."""

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        """
        GET requests are available to speakers, organizers, and admins
        POST requests are available to authenticated attendees
        """
        if self.request.method == "GET":
            return [IsSpeakerOrOrganizerOrAdmin()]
        return [IsAttendee()]  # Only attendees should create feedback


@extend_schema(request=FeedbackSerializer, responses=FeedbackSerializer(many=True))
class FeedbackDetailView(RetrieveUpdateDestroyAPIView):
    """retrieve, delete and update endpoint for feedbacks."""

    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def get_permissions(self):
        """
        GET requests are available to speakers, organizers, and admins
        PUT, PATCH, DELETE requests are available to organizers and admins
        """
        if self.request.method == "GET":
            return [IsSpeakerOrOrganizerOrAdmin()]
        return [IsSpeakerOrOrganizerOrAdmin()]
