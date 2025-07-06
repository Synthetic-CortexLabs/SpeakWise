"""Speaker views."""

from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from .models import SkillTag
from .models import SpeakerDashboard
from .models import SpeakerProfile
from .models import SpeakerSocialLink
from .serializers import SkillTagSerializer
from .serializers import SpeakerDashboardSerializer
from .serializers import SpeakerProfileSerializer
from .serializers import SpeakerSocialLinkSerializer
from .serializers import SpeakerSerializer
from speakwise.authentication.permissions import (
    IsSpeaker,
    IsOrganizerOrAdmin,
    IsSpeakerOrOrganizerOrAdmin,
)
from speakwise.users.choices import UserRoles


class SpeakerProfileList(generics.ListCreateAPIView):
    """List all speaker profiles or create a new one."""

    queryset = SpeakerProfile.objects.all()
    serializer_class = SpeakerProfileSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        POST requests are available to organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsOrganizerOrAdmin()]


class SpeakerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a speaker profile."""

    queryset = SpeakerProfile.objects.all()
    serializer_class = SpeakerProfileSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        PUT, PATCH, DELETE requests are available to:
        - The speaker themselves
        - Organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsSpeakerOrOrganizerOrAdmin()]

    def check_object_permissions(self, request, obj):
        """
        Check if speaker has permission to edit their own profile
        """
        super().check_object_permissions(request, obj)

        # Skip permission check for GET requests (they're already allowed by AllowAny)
        if request.method == "GET":
            return

        # If user has organizer or admin role, they're already allowed
        if (
            hasattr(request.user, "role")
            and request.user.role
            and request.user.role.display in [UserRoles.ORGANIZER, UserRoles.ADMIN]
        ):
            return

        # If user is the speaker of this profile, allow access
        if obj.speaker_user == request.user:
            return

        # Otherwise, deny access
        self.permission_denied(
            request, message="You don't have permission to edit this speaker profile."
        )


class SkillTagList(generics.ListCreateAPIView):
    """List all skill tags or create a new one."""

    queryset = SkillTag.objects.all()
    serializer_class = SkillTagSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        POST requests are available only to speakers, organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsSpeakerOrOrganizerOrAdmin()]


class SkillTagDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a skill tag."""

    queryset = SkillTag.objects.all()
    serializer_class = SkillTagSerializer

    def get_permissions(self):
        """
        GET request is available to everyone
        PUT, PATCH, DELETE requests are available only to organizers and admins
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsOrganizerOrAdmin()]


class SpeakerSocialLinkList(generics.ListCreateAPIView):
    """List all social links for authenticated user or create a new one."""

    serializer_class = SpeakerSocialLinkSerializer

    def get_permissions(self):
        """Only speakers can manage their social links."""
        return [IsSpeaker()]

    def get_queryset(self):
        return SpeakerSocialLink.objects.filter(speaker__user=self.request.user)

    def perform_create(self, serializer):
        try:
            speaker_profile = SpeakerProfile.objects.get(user=self.request.user)
            serializer.save(speaker=speaker_profile)
        except SpeakerProfile.DoesNotExist:
            self.permission_denied(
                self.request,
                message="You must have a speaker profile to add social links.",
            )


class SpeakerSocialLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a social link."""

    serializer_class = SpeakerSocialLinkSerializer

    def get_permissions(self):
        """Only speakers can manage their social links."""
        return [IsSpeaker()]

    def get_queryset(self):
        return SpeakerSocialLink.objects.filter(speaker__user=self.request.user)


class SpeakerDashboardView(generics.RetrieveAPIView):
    """Get dashboard information for a speaker."""

    queryset = SpeakerProfile.objects.all()
    serializer_class = SpeakerDashboardSerializer

    def get_permissions(self):
        """
        GET request is available to:
        - The speaker themselves
        - Organizers and admins
        """
        return [IsSpeakerOrOrganizerOrAdmin()]

    def check_object_permissions(self, request, obj):
        """
        Check if speaker has permission to view their own dashboard
        """
        super().check_object_permissions(request, obj)

        # If user has organizer or admin role, they're already allowed
        if (
            hasattr(request.user, "role")
            and request.user.role
            and request.user.role.display in [UserRoles.ORGANIZER, UserRoles.ADMIN]
        ):
            return

        # If user is the speaker of this dashboard, allow access
        if obj.user == request.user:
            return

        # Otherwise, deny access
        self.permission_denied(
            request, message="You don't have permission to view this speaker dashboard."
        )

    @extend_schema(
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


@api_view(["GET", "PATCH"])
@permission_classes([IsAuthenticated])
def speaker_profile_me(request):
    """Get or update the current speaker's profile."""
    try:
        speaker_profile = SpeakerProfile.objects.get(speaker_user=request.user)
    except SpeakerProfile.DoesNotExist:
        return Response(
            {"error": "Speaker profile not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serializer = SpeakerProfileSerializer(speaker_profile)
        return Response(serializer.data)

    elif request.method == "PATCH":
        serializer = SpeakerProfileSerializer(
            speaker_profile, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def speaker_upload_avatar(request):
    """Upload avatar for the current speaker."""
    try:
        speaker_profile = SpeakerProfile.objects.get(speaker_user=request.user)
    except SpeakerProfile.DoesNotExist:
        return Response(
            {"error": "Speaker profile not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if "avatar" not in request.FILES:
        return Response(
            {"error": "No avatar file provided"}, status=status.HTTP_400_BAD_REQUEST
        )

    speaker_profile.avatar = request.FILES["avatar"]
    speaker_profile.save()

    serializer = SpeakerProfileSerializer(speaker_profile)
    return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def skill_tags_list_create(request):
    """List all skill tags or create a new one."""
    if request.method == "GET":
        skill_tags = SkillTag.objects.all()
        serializer = SkillTagSerializer(skill_tags, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SkillTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
