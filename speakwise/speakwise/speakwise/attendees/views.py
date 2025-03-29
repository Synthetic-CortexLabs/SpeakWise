"""attendees views."""

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from speakwise.attendees.models import Attendee
from speakwise.attendees.serializers import AttendeeSerializer
from speakwise.attendees.serializers import VerifyAttendeeWithEmailSerializer
from speakwise.organizers.models import AttendanceEmails


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


@extend_schema(
    request=VerifyAttendeeWithEmailSerializer,
    responses=VerifyAttendeeWithEmailSerializer,
)
class ValidateAttendeeView(APIView):
    """Verify attendee with email."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Verify attendee with email."""
        email = request.data.get("email")
        try:
            AttendanceEmails.objects.get(email=email)
        except AttendanceEmails.DoesNotExist:
            return Response(
                "Attendee with the specified email does not exist",
                status=status.HTTP_404_NOT_FOUND,
            )
        # redirect attendee to feedback page to give feedback
        return Response(email, status=200)
