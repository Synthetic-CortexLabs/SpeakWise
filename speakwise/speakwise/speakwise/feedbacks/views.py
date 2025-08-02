"""feedback views."""

from django.db.models import Avg
from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from speakwise.authentication.permissions import IsSpeakerOrOrganizerOrAdmin
from speakwise.events.models import Session
from speakwise.feedbacks.models import Feedback
from speakwise.feedbacks.serializers import FeedbackSerializer


@extend_schema(request=FeedbackSerializer, responses=FeedbackSerializer(many=True))
class FeedbackListCreateView(ListCreateAPIView):
    """Feedback list and create api endpoint."""

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        """
        GET requests are available to speakers, organizers, and admins
        POST requests are available to anyone (for anonymous feedback)
        """
        if self.request.method == "GET":
            return [IsSpeakerOrOrganizerOrAdmin()]
        return [AllowAny()]  # Allow anonymous feedback submissions


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


@api_view(["GET"])
@permission_classes([AllowAny])
def speaker_feedback_view(request, speaker_id):
    """Get all feedback for a specific speaker (anonymous)."""
    try:
        # Get all sessions for this speaker
        speaker_sessions = Session.objects.filter(speaker__id=speaker_id)

        # Get all feedback for these sessions
        feedback_queryset = (
            Feedback.objects.filter(session__in=speaker_sessions)
            .select_related("session", "session__event")
            .order_by("-created_at")
        )

        # Calculate statistics
        stats = feedback_queryset.aggregate(
            total_feedback=Count("id"),
            avg_overall=Avg("overall_rating"),
            avg_engagement=Avg("engagement"),
            avg_clarity=Avg("clarity"),
            avg_content_depth=Avg("content_depth"),
            avg_speaker_knowledge=Avg("speaker_knowledge"),
            avg_practical_relevance=Avg("practical_relevance"),
        )

        # Prepare feedback data (anonymized)
        feedback_data = []
        for feedback in feedback_queryset:
            feedback_data.append(
                {  # noqa: PERF401
                    "id": feedback.id,
                    "session_name": feedback.session.name,
                    "event_name": feedback.session.event.title,
                    "overall_rating": feedback.overall_rating,
                    "engagement": feedback.engagement,
                    "clarity": feedback.clarity,
                    "content_depth": feedback.content_depth,
                    "speaker_knowledge": feedback.speaker_knowledge,
                    "practical_relevance": feedback.practical_relevance,
                    "comment": (
                        feedback.comment
                        if not feedback.is_anonymous
                        else feedback.comment
                    ),
                    "is_anonymous": feedback.is_anonymous,
                    "created_at": feedback.created_at,
                }
            )

        return Response(
            {
                "stats": {
                    "total_feedback": stats["total_feedback"] or 0,
                    "avg_overall": round(stats["avg_overall"] or 0, 2),
                    "avg_engagement": round(stats["avg_engagement"] or 0, 2),
                    "avg_clarity": round(stats["avg_clarity"] or 0, 2),
                    "avg_content_depth": round(stats["avg_content_depth"] or 0, 2),
                    "avg_speaker_knowledge": round(
                        stats["avg_speaker_knowledge"] or 0, 2
                    ),
                    "avg_practical_relevance": round(
                        stats["avg_practical_relevance"] or 0, 2
                    ),
                },
                "feedback": feedback_data,
                "total_sessions": speaker_sessions.count(),
            }
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
