"""attendees views."""

from http.client import responses
from warnings import catch_warnings

from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from speakwise.attendees.models import Attendee
from speakwise.attendees.serializers import AttendeeSerializer


@extend_schema(request=AttendeeSerializer, responses=AttendeeSerializer)
class AttendeeListCreateView(ListCreateAPIView):
    serializer_class = AttendeeSerializer
    permission_classes = [AllowAny]
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [AllowAny]
    queryset = Attendee.objects.all()


@extend_schema(request=AttendeeSerializer, responses=AttendeeSerializer)
class AttendeeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AttendeeSerializer
    permission_classes = [AllowAny]
    queryset = Attendee.objects.all()
