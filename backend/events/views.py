"""This module contains the views for the events app."""

from rest_framework.permissions import AllowAny
from .models import Event
from .serializers import EventsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema


@extend_schema(request=EventsSerializer, responses={200, EventsSerializer(many=True)})
class EventCreateView(ListCreateAPIView):
    """Event list and create api endpoint."""

    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventsSerializer


@extend_schema(responses={200, EventsSerializer(many=True)})
class EventListView(RetrieveUpdateDestroyAPIView):
    """retrieve, delete and update endpoint for events."""

    queryset = Event.objects.all()
    permission_classes = [AllowAny]
    serializer_class = EventsSerializer
