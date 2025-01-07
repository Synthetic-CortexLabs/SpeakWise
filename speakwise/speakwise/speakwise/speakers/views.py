"""Speaker views."""

from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import SpeakerProfile, SkillTag, SpeakerSocialLink, SpeakerDashboard
from .serializers import (
    SpeakerProfileSerializer, SkillTagSerializer,
    SpeakerSocialLinkSerializer, SpeakerDashboardSerializer
)

class SpeakerProfileList(generics.ListCreateAPIView):
    """List all speaker profiles or create a new one."""
    queryset = SpeakerProfile.objects.all()
    serializer_class = SpeakerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SpeakerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a speaker profile."""
    queryset = SpeakerProfile.objects.all()
    serializer_class = SpeakerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SkillTagList(generics.ListCreateAPIView):
    """List all skill tags or create a new one."""
    queryset = SkillTag.objects.all()
    serializer_class = SkillTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SkillTagDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a skill tag."""
    queryset = SkillTag.objects.all()
    serializer_class = SkillTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SpeakerSocialLinkList(generics.ListCreateAPIView):
    """List all social links for authenticated user or create a new one."""
    serializer_class = SpeakerSocialLinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SpeakerSocialLink.objects.filter(speaker__speaker_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(speaker=self.request.user.speaker_profile)

class SpeakerSocialLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a social link."""
    serializer_class = SpeakerSocialLinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SpeakerSocialLink.objects.filter(speaker__speaker_user=self.request.user)

@api_view(['GET'])
def speaker_dashboard(request, pk):
    """Get dashboard information for a speaker."""
    try:
        speaker = SpeakerProfile.objects.get(pk=pk)
        dashboard = SpeakerDashboard.objects.get(speaker_profile=speaker)
        serializer = SpeakerDashboardSerializer(dashboard)
        return Response(serializer.data)
    except SpeakerProfile.DoesNotExist:
        return Response(status=404)
