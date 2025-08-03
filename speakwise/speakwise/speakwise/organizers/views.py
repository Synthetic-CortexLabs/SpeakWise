"""organizers views."""

import csv
import io
import os

from django.http import Http404
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from speakwise.authentication.permissions import IsOrganizer
from speakwise.authentication.permissions import IsOrganizerOrAdmin
from speakwise.users.choices import UserRoles

from .models import AttendanceEmails
from .models import Organizers
from .serializers import FileUploadSerializer
from .serializers import OrganizerSerializer
from .services import FileHandler


@extend_schema(
    tags=["Organizers"],
    request=OrganizerSerializer,
    responses={200: OrganizerSerializer},
)
class OrganizerListCreateView(generics.ListCreateAPIView):
    """List all organizers or create a new organizer"""

    queryset = Organizers.objects.all()
    serializer_class = OrganizerSerializer

    def get_permissions(self):
        """
        GET requests can be made by anyone
        POST requests only by admins (who can create organizers)
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsOrganizerOrAdmin()]


@extend_schema(
    tags=["Organizers"],
    request=OrganizerSerializer,
    responses={200: OrganizerSerializer},
)
class OrganizerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an organizer"""

    queryset = Organizers.objects.all()
    serializer_class = OrganizerSerializer
    permission_classes = [IsOrganizerOrAdmin]


class FileUploadViewCreatView(APIView):
    """File upload view."""

    permission_classes = [IsOrganizerOrAdmin]
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def post(self, request, *args, **kwargs):
        """Process the uploaded file."""

        file_obj = request.FILES.get("file")
        event_id = request.data.get("event")

        if not file_obj:
            return Response(
                {"error": "No file provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not event_id:
            return Response(
                {"error": "Event ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get the event object
        try:
            from speakwise.events.models import Event
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Process the file with your FileHandler
        file_handler = FileHandler()

        temp_file_path = file_handler.clean_file(file_obj)

        try:
            file_handler.extract_emails(temp_file_path, event=event)
        except Exception as e:
            os.remove(temp_file_path)
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        os.remove(temp_file_path)
        attendance_list = AttendanceEmails.objects.filter(event=event)
        serializer = FileUploadSerializer(attendance_list, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(responses=FileUploadSerializer(many=True))
    def get(self, request):
        """Get all attendance emails."""

        emails = AttendanceEmails.objects.all()
        serializer = FileUploadSerializer(emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FileUploadDetailview(APIView):
    """File upload detail view."""

    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return AttendanceEmails.objects.get(pk=pk)
        except AttendanceEmails.DoesNotExist as err:
            raise Http404 from err

    @extend_schema(responses={200: FileUploadSerializer})
    def patch(self, request, pk=None):
        """update an email."""
        email = self.get_object(pk)
        serializer = FileUploadSerializer(
            email, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(responses={204: None})
    def delete(self, request, pk):
        """Delete an attendance email."""
        email = self.get_object(pk)
        email.delete()
        return Response(
            {"message": "Email deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
