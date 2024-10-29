"""Speaker views."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .models import Speaker
from .serializers import SpeakerSerializer


class SpeakerListCreateView(generics.ListCreateAPIView):
    """Speaker list and create api endpoint."""

    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroySpeakerView(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, delete and update endpoint for speakers."""

    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAuthenticated]
