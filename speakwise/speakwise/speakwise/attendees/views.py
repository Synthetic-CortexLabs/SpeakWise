"""attendees views."""

from rest_framework.permissions import AllowAny
from speakwise.attendees.serializers import AttendeeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from speakwise.attendees.models import Attendee


@extend_schema(request=AttendeeSerializer, responses=AttendeeSerializer)
class AttendeeListCreateView(ListCreateAPIView):
	serializer_class = AttendeeSerializer
	permission_classes = [AllowAny]
	queryset = Attendee.objects.all()


@extend_schema(request=AttendeeSerializer, responses=AttendeeSerializer)
class AttendeeDetailView(RetrieveUpdateDestroyAPIView):
	serializer_class = AttendeeSerializer
	permission_classes = [AllowAny]
	queryset = Attendee.objects.all()