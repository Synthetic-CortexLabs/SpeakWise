"""Tests for events app."""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from speakwise.events.models import Event

from speakwise.attendees.models import Attendee, AttendanceCode

from speakwise.attendees.views import AttendeeListCreateView, AttendeeDetailView


class TestModels(TestCase):
    """Test models."""

    def test_attendees_model(self):
        """Test Event model."""
        attendee = Attendee.objects.create(email="user@mail.com")
        assert attendee.email == "user@mail.com"
        assert attendee.first_name == None
        assert attendee.last_name == None
        assert attendee.is_verified == False

    def test_country_model(self):
        """Test Country model."""

        event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            location="Test Location",
            is_active=True,
        )
        attendee = Attendee.objects.create(email="admin@mail.com")
        att_code = AttendanceCode.objects.create(
            attendee=attendee, event=event, code="2024SW"
        )
        assert att_code.code == "2024SW"
        assert att_code.event == event
        assert att_code.attendee == attendee
        assert type(att_code.code) is not int