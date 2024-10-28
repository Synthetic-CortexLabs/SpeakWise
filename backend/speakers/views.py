from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .models import Speaker
from .serializers import SpeakerSerializer

class SpeakerListCreateView(generics.ListCreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAuthenticated]



