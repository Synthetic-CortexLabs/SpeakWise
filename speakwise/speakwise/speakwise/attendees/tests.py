"""Tests for events app."""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from speakwise.attendees.models import AttendanceCode
from speakwise.attendees.models import Attendee
from speakwise.events.models import Event


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
            attendee=attendee,
            event=event,
            code="2024SW",
        )
        assert att_code.code == "2024SW"
        assert att_code.event == event
        assert att_code.attendee == attendee
        assert type(att_code.code) is not int


class ValidateAttendeeViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_email = "valid@example.com"
        self.invalid_email = "invalid@example.com"
        self.url = reverse('verify-attendee')

        # Create a sample attendee in the database
        self.attendee = Attendee.objects.create(email=self.valid_email)

    def test_validate_attendee_with_valid_email(self):
        """Test validation with an email that exists in the database."""
        response = self.client.post(self.url, {"email": self.valid_email})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.valid_email)

    def test_validate_attendee_with_invalid_email(self):
        """Test validation with an email that does not exist in the database."""
        response = self.client.post(self.url, {"email": self.invalid_email})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
