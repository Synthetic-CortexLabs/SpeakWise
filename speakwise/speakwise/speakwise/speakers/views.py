"""Speaker views."""

from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .models import Speaker
from .serializers import SpeakerSerializer


@extend_schema(request=SpeakerSerializer, responses=SpeakerSerializer(many=True))
class SpeakerListCreateView(generics.ListCreateAPIView):
    """Speaker list and create api endpoint."""

    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(responses={200, SpeakerSerializer})
class RetrieveUpdateDestroySpeakerView(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, delete and update endpoint for speakers."""

    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAuthenticated]
