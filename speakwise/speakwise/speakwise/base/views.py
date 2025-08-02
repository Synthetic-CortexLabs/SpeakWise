"""Team views for the SpeakWise application."""

from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import TeamMemberSerializer
from .models import TeamMember


@extend_schema(
    tags=["Team"],
    responses={200: TeamMemberSerializer(many=True)},
)
class TeamMemberListView(generics.ListAPIView):
    """List all active team members."""

    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]  # Public endpoint

    def get_serializer_context(self):
        """Add request to serializer context for building absolute URLs."""
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
