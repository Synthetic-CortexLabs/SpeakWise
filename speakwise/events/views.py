"""Events views."""

from django.db.models import ProtectedError
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Event
from .models import Session
from .serializers import EventSerializer
from .serializers import SessionSerializer


@extend_schema(request=EventSerializer, responses={200: EventSerializer})
class EventListCreateAPIView(ListCreateAPIView):
    """View for listing and creating events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: EventSerializer})
class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting events."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {"message": "Event deleted successfully"},
                status=status.HTTP_200_OK
            )
        except ProtectedError:
            return Response(
                {"error": "Cannot delete event with active sessions"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:  # noqa: BLE001
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

@extend_schema(request=SessionSerializer, responses={200: SessionSerializer})
class SessionListCreateAPIView(ListCreateAPIView):
    """View for listing and creating sessions."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: SessionSerializer})
class SessionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting sessions."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (AllowAny,)
