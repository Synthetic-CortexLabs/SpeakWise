"""organizers views."""

import os

from django.http import Http404
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AttendanceEmails
from .models import Organizers
from .serializers import  AttendanceSerializer
from .serializers import OrganizerSerializer
from .services import FileHandler
from speakwise.authentication.permissions import (
    IsOrganizerOrAdmin,
)


@extend_schema(
    tags=["Organizers"],
    request=OrganizerSerializer,
    responses={200: OrganizerSerializer},
)
class OrganizerListCreateView(generics.ListCreateAPIView):
    """List all organizers or create a new organizer"""

    queryset = Organizers.objects.all()
    serializer_class = OrganizerSerializer
    permission_classes = [AllowAny]

    # def get_permissions(self):
    #     """
    #     GET requests can be made by anyone
    #     POST requests only by admins (who can create organizers)
    #     """
        # if self.request.method == "GET":
        #     return [AllowAny()]
        # return [IsOrganizerOrAdmin()]


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

    # permission_classes = [IsOrganizerOrAdmin]
    permission_classes = [AllowAny]
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def post(self, request, *args, **kwargs):
        """Process the uploaded file."""

        file_obj = request.FILES.get("file")
        event = request.data.get("event")

        print(file_obj)
        # Process the file with your FileHandler
        file_handler = FileHandler()

        temp_file_path = file_handler.clean_file(file_obj)
        print(temp_file_path)

        try:
            file_handler.extract_emails(temp_file_path, event=event)
        except Exception as e:
            os.remove(temp_file_path)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        os.remove(temp_file_path)
        attendance_list = AttendanceEmails.objects.filter(event=event)
        serializer = AttendanceSerializer(data=attendance_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(responses=AttendanceSerializer(many=True))
    def get(self, request):
        """Get all attendance emails."""

        emails = AttendanceEmails.objects.all()
        serializer = AttendanceSerializer(emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FileUploadDetailview(APIView):
    """File upload detail view."""

    permission_classes = [AllowAny]

    def get_object(self, pk):
        """get attendance instance."""
        try:
            return AttendanceEmails.objects.get(pk=pk)
        except AttendanceEmails.DoesNotExist as err:
            raise Http404 from err

    @extend_schema(responses={200: AttendanceSerializer})
    def patch(self, request, pk=None):
        """update an email."""
        email = self.get_object(pk)
        serializer = AttendanceSerializer(email, data=request.data, partial=True)
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
