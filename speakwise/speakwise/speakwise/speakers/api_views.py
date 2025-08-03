"""Speaker API views for profile management."""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from speakwise.authentication.permissions import IsSpeaker

from .models import SkillTag, SpeakerProfile
from .serializers import SkillTagSerializer, SpeakerProfileSerializer


@api_view(["GET", "PATCH"])
@permission_classes([IsAuthenticated, IsSpeaker])
def speaker_profile_me(request):
    """Get or update the current speaker's profile."""
    try:
        speaker_profile = SpeakerProfile.objects.get(speaker_user=request.user)
    except SpeakerProfile.DoesNotExist:
        return Response(
            {"error": "Speaker profile not found. Please contact admin."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serializer = SpeakerProfileSerializer(speaker_profile)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = SpeakerProfileSerializer(
            speaker_profile,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsSpeaker])
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
            {"error": "No avatar file provided"},
            status=status.HTTP_400_BAD_REQUEST,
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

    if request.method == "POST":
        serializer = SkillTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
