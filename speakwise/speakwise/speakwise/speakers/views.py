"""Speaker views."""

from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import SkillTag
from .models import SpeakerDashboard
from .models import SpeakerProfile
from .models import SpeakerSocialLink
from .serializers import SkillTagSerializer
from .serializers import SpeakerDashboardSerializer
from .serializers import SpeakerProfileSerializer
from .serializers import SpeakerSocialLinkSerializer
from drf_spectacular.utils import extend_schema


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


class SpeakerDashboardView(generics.RetrieveAPIView):
    """Get dashboard information for a speaker."""

    queryset = SpeakerProfile.objects.all()
    serializer_class = SpeakerDashboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @extend_schema(
        operation_id="get_speaker_dashboard",
        description="Get dashboard information for a speaker",
        responses={200: SpeakerDashboardSerializer},
    )
    def get(self, request, *args, **kwargs):
        speaker = self.get_object()
        try:
            dashboard = SpeakerDashboard.objects.get(speaker_profile=speaker)
            serializer = self.get_serializer(dashboard)
            return Response(serializer.data)
        except SpeakerDashboard.DoesNotExist:
            raise NotFound("Dashboard not found for this speaker")
