"""feedback tests."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from speakwise.attendees.models import Attendee
from speakwise.events.models import Event
from speakwise.events.models import Session
from speakwise.feedbacks.models import Feedback


class SETUP(TestCase):
    """Test feedback model."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            name="testuser",
            password="password123",
            email="user@mail.com",
        )
        self.attendee = Attendee.objects.create(
            first_name="Test",
            last_name="User",
            email="attendee@mail.com",
            is_verified=True,
        )
        self.event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            start_date_time="2021-01-01T10:00:00Z",
            end_date_time="2021-01-02T10:00:00Z",
        )
        self.session = Session.objects.create(
            name="Test Session",
            description="This is a test session.",
            start_date_time="2021-01-01T10:00:00Z",
            end_date_time="2021-01-02T10:00:00Z",
            event=self.event,
        )
        self.feedback = Feedback.objects.create(
            engagement=5,
            clarity=5,
            content_depth=5,
            speaker_knowledge=5,
            practical_relevance=5,
            overall_rating=5,
            attendee=self.attendee,
            session=self.session,
        )
        self.client = APIClient()
        self.list_view = reverse("feedbacks:list_view")
        self.detail_view = reverse("feedbacks:detail_view", args=[self.feedback.pk])


class TestFeedbackModel(SETUP):
    def test_feedback_creation(self):
        """Test feedback creation."""

        assert self.feedback.engagement == 5
        assert self.feedback.attendee == self.attendee
        assert self.feedback.session == self.session
        assert self.feedback.overall_rating == 5


class TestFeedbackViews(SETUP):
    """test feedback views."""

    def test_feedback_list_view(self):
        """test feedback list view."""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.list_view)
        assert response.status_code == status.HTTP_200_OK

    def test_feedback_detail_view(self):
        """test feedback detail view."""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.detail_view)
        assert response.status_code == status.HTTP_200_OK

    def test_feedback_create_view(self):
        """test feedback create view."""

        self.client.force_authenticate(user=self.user)

        data = {
            "engagement": 5,
            "clarity": 5,
            "content_depth": 5,
            "speaker_knowledge": 5,
            "practical_relevance": 5,
            "overall_rating": 5,
            "attendee": self.attendee.pk,
            "session": self.session.pk,
        }

        response = self.client.post(self.list_view, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get("engagement") == 5
        assert response.data.get("attendee") == self.attendee.pk
        assert response.data.get("session") == self.session.pk
