"""teams views."""

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from speakwise.teams.models import TeamMember
from speakwise.teams.serializers import TeamMemberSerializer


class TeamMemberListView(APIView):
    """View to list all team members."""

    permission_classes = [AllowAny]

    @extend_schema(
        summary="List Team Members",
        description="Retrieve a list of all active team members.",
        responses={200: TeamMemberSerializer(many=True)},
    )
    def get(self, request):
        """Handle GET requests to retrieve team members."""
        team_members = TeamMember.objects.filter(is_active=True)
        serializer = TeamMemberSerializer(team_members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
