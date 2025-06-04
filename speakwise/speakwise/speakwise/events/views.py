"""Events views."""

from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import Country
from .models import Event
from .models import Region
from .models import Session
from .serializers import CountrySerializer
from .serializers import EventSerializer
from .serializers import RegionSerializer
from .serializers import SessionSerializer
from .serializers import TagSerializer
from .models import Tag


@extend_schema(request=RegionSerializer, responses={200: RegionSerializer})
class RegionListCreateAPIView(ListCreateAPIView):
    """View for listing and creating regions."""

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: RegionSerializer})
class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting regions."""

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (AllowAny,)


@extend_schema(request=CountrySerializer, responses={200: CountrySerializer})
class CountryListCreateAPIView(ListCreateAPIView):
    """View for listing and creating countries."""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """Filter countries by region if region parameter is provided."""
        queryset = Country.objects.all()
        region_id = self.request.query_params.get("region")

        if region_id:
            queryset = queryset.filter(region_id=region_id)

        return queryset


@extend_schema(responses={200: CountrySerializer})
class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting countries."""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


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


@extend_schema(request=TagSerializer, responses={200: TagSerializer})
class TagListCreateAPIView(ListCreateAPIView):
    """View for listing and creating tags."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


@extend_schema(responses={200: TagSerializer})
class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting tags."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
