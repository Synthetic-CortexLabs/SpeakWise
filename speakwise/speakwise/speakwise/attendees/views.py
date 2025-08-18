"""attendees views."""

from django.shortcuts import get_object_or_404
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
from speakwise.authentication.permissions import IsAttendee
from speakwise.authentication.permissions import IsOrganizerOrAdmin
from speakwise.organizers.models import AttendanceEmails
from speakwise.users.choices import UserRoles


@extend_schema(request=AttendeeSerializer, responses=AttendeeSerializer)
class AttendeeListCreateView(ListCreateAPIView):
    """View for listing and creating attendees."""

    serializer_class = AttendeeSerializer
    queryset = Attendee.objects.all()

    def get_permissions(self):
        """
        GET request is available to organizers and admins
        POST request is available to anyone (to register as an attendee)
        """
        if self.request.method == "GET":
            return [IsOrganizerOrAdmin()]
        return [AllowAny()]


@extend_schema(request=AttendeeSerializer, responses=AttendeeSerializer)
class AttendeeDetailView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating and deleting an attendee."""

    serializer_class = AttendeeSerializer
    queryset = Attendee.objects.all()

    def get_permissions(self):
        """
        GET, PUT, PATCH, DELETE requests are available to:
        - The attendee accessing their own profile
        - Organizers and admins
        """
        # Using separate permission classes instead of the | operator
        return [IsAttendee(), IsOrganizerOrAdmin()]

    def check_object_permissions(self, request, obj):
        """Check if attendee has permission to access their own profile."""
        super().check_object_permissions(request, obj)

        # Organizers and admins can access any attendee profile
        if request.user.role and request.user.role.display in [  # should we really do this?
            UserRoles.ORGANIZER,
            UserRoles.ADMIN,
        ]:
            return

        # Attendees can only access their own profile
        if obj.user == request.user:
            return

        # Otherwise, deny permission
        self.permission_denied(
            request,
            message="You don't have permission to access this profile.",
        )


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


@extend_schema(responses=AttendeeSerializer)
class AttendeeByEmailView(APIView):
    """Get attendee by email address."""

    permission_classes = [AllowAny]

    def get(self, request, email):
        """Get attendee by email address."""
        attendee = get_object_or_404(Attendee, email=email)
        serializer = AttendeeSerializer(attendee)
        return Response(serializer.data, status=status.HTTP_200_OK)
