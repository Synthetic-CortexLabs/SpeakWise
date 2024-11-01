"""Talks views module."""

from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from speakwise.talks.models import Talks
from speakwise.talks.serializers import TalkSerializer

"""Events views."""


@extend_schema(request=TalkSerializer, responses={200: TalkSerializer})
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
