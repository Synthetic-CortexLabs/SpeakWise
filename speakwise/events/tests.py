"""Tests for events app."""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .models import Country
from .models import Event
from .models import Region
from .models import Session
from .views import EventListCreateAPIView


class TestModels(TestCase):
    """Test models."""

    def test_event_model(self):
        """Test Event model."""
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            location="Test Location",
            is_active=True,
        )
        assert event.title == "Test Event"
        assert event.description == "This is a test event."
        assert event.location == "Test Location"
        assert event.is_active == True
        assert str(event) == "Test Event"

    def test_country_model(self):
        """Test Country model."""
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            location="Test Location",
            is_active=True,
        )
        country = Country.objects.create(
            name="Test Country",
            event=event,
        )
        assert country.name == "Test Country"
        assert country.event == event
        assert country.region_set.count() == 0
        assert str(country) == "Test Country"

    def test_region_model(self):
        """Test Region model."""
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            location="Test Location",
            is_active=True,
        )
        country = Country.objects.create(
            name="Test Country",
            event=event,
        )
        region = Region.objects.create(
            name="Test Region",
            country=country,
        )
        assert region.name == "Test Region"
        assert region.country == country
        assert str(region) == "Test Region"

    def test_session_model(self):
        """Test Session model."""
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            location="Test Location",
            is_active=True,
        )
        session = Session.objects.create(
            name="Test Session",
            description="This is a test session.",
            start_date_time="2022-01-01T00:00:00Z",
            end_date_time="2022-01-01T01:00:00Z",
            event=event,
            location="Test Location",
        )
        assert session.name == "Test Session"
        assert session.description == "This is a test session."
        assert session.start_date_time == "2022-01-01T00:00:00Z"
        assert session.end_date_time == "2022-01-01T01:00:00Z"
        assert session.event == event
        assert session.location == "Test Location"
        assert str(session) == "Test Session"


class TestViews(APITestCase):
    """test views."""

    def test_event_list_create_api_view(self):
        """Test EventListCreateAPIView."""
        factory = APIRequestFactory()
        request = factory.get(reverse("events:event-list-create"))
        view = EventListCreateAPIView.as_view()
        response = view(request)
        assert response.status_code == status.HTTP_200_OK
