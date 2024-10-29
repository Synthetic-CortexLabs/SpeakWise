"""Test events app."""

from django.test import TestCase
from .views import EventListView, EventCreateView
from django.urls import reverse, resolve
from django.utils import timezone
from .models import Event


class TestEventsDB(TestCase):
    """Test events database."""

    def test_create_event(self):
        """test creating an event."""
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event",
            start_date=timezone.now(),
            end_date=timezone.now(),
            location="Test Location",
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        self.assertEqual(event.title, "Test Event")
        self.assertEqual(event.description, "This is a test event")
        self.assertEqual(event.location, "Test Location")


class TestEventViews(TestCase):
    """Test event views."""

    def test_event_list_view(self):
        """test that the event list view is working."""
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event",
            start_date=timezone.now(),
            end_date=timezone.now(),
            location="Test Location",
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        response = self.client.get(
            reverse("events:event_list", kwargs={"pk": event.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event")
        self.assertEqual(response.resolver_match.func.view_class, EventListView)

    def test_event_create_view(self):
        """test that the event create view is working."""
        response = self.client.get(reverse("events:event_create"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.view_class, EventCreateView)

    def test_event_list_url_resolves_event_list_view(self):
        """test that the event list url resolves to the event list view."""
        view = resolve("/api/events/")
        self.assertEqual(view.func.view_class, EventCreateView)

    def test_updated_event(self):
        """test updating an event."""
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event",
            start_date=timezone.now(),
            end_date=timezone.now(),
            location="Test Location",
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        new_event = Event.objects.get(id=event.id)
        new_event.title = "Updated Test Event"
        new_event.description = "This is an updated test event"
        new_event.location = "Updated Test Location"

        self.assertEqual(new_event.title, "Updated Test Event")
        self.assertEqual(new_event.description, "This is an updated test event")
        self.assertEqual(new_event.location, "Updated Test Location")
