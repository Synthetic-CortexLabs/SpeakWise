# Create your views here.
# organizers/views.py
import os

from django.http import Http404
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
    permission_classes = [AllowAny]


@extend_schema(
    tags=["Organizers"],
    request=OrganizerSerializer,
    responses={200: OrganizerSerializer},
)
class OrganizerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an organizer"""

    queryset = Organizers.objects.all()
    serializer_class = OrganizerSerializer
    permission_classes = [IsAuthenticated]


class FileUploadViewCreatView(APIView):
    """File upload view."""

    permission_classes = [AllowAny]
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def post(self, request, *args, **kwargs):
        """Process the uploaded file."""

        file_obj = request.FILES.get("file")
        event = request.data.get("event")

        # Process the file with your FileHandler
        file_handler = FileHandler()

        temp_file_path = file_handler.clean_file(file_obj)

        try:
            file_handler.extract_emails(temp_file_path, event=event)
        except Exception as e:
            os.remove(temp_file_path)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        os.remove(temp_file_path)
        return Response(
            {"message": "File processed successfully."},
            status=status.HTTP_200_OK,
        )

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

    def delete(self, request, pk):
        """Delete an attendance email."""
        email = self.get_object(pk)
        email.delete()
        return Response(
            {"message": "Email deleted successfully."},
            status=status.HTTP_200_OK,
        )
