from rest_framework import generics
from rest_framework.permissions import AllowAny
from talks.models import Talks
from talks.serializers import TalkSerializer


class TalkListCreateView(generics.ListCreateAPIView):
    """
    View to list all talks and create a new talk.
    """
    queryset = Talks.objects.all()
    serializer_class = TalkSerializer
    permission_classes = [AllowAny]


class TalkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a talk.
    """
    queryset = Talks.objects.all()
    serializer_class = TalkSerializer
    permission_classes = [AllowAny]
