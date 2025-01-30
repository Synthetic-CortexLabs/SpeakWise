"""attendees views."""
from http.client import responses
from warnings import catch_warnings

from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from speakwise.attendees.models import Attendee
from speakwise.attendees.serializers import AttendeeSerializer, VerifyAttendeeWithEmailSerializer


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


@extend_schema(request=VerifyAttendeeWithEmailSerializer,responses=VerifyAttendeeWithEmailSerializer)
class ValidateAttendeeView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
            serializer = VerifyAttendeeWithEmailSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                try:
                    attendee = Attendee.objects.get(email=email)
                except Attendee.DoesNotExist:
                    return Response("Attendee with the specified email does not exist",status=404)
                return Response(email,status=200)
            return Response(serializer.errors,status=400)
