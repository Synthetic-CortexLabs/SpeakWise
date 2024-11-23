# Create your views here.
# organizers/views.py
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Organizers
from .serializers import OrganizerSerializer


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
