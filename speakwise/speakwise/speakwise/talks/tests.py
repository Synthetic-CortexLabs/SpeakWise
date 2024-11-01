"""Talks app tests."""

from datetime import datetime
from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from events.models import Event
from rest_framework import status
from rest_framework.test import APIClient
from speakers.models import Speaker
from talks.models import Talks
from talks.serializers import TalkSerializer


class TalksModelTest(TestCase):
    """Test the Talks model."""

    def setUp(self):
        """Set up the test."""
        self.user = User.objects.create_user(
            username="testuser", password="testpass")
        self.event = Event.objects.create(
            title="Test Event",
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=1),
        )
        self.speaker = Speaker.objects.create(
            user_id=self.user,
            twitter="test_twitter",
            organization="Test Organization",
            bio="Test Bio",
            avatar="path/to/avatar.jpg",
        )
        self.talk = Talks.objects.create(
            event_id=self.event,
            title="Test Talk",
            description="Test Description",
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(hours=1),
        )
        self.talk.speaker_id.add(self.speaker)

    def test_talk_creation(self):
        """Test the talk creation."""
        self.assertEqual(self.talk.title, "Test Talk")


class TalksAPITest(TestCase):
    """Test the Talks API."""

    def setUp(self):
        """Set up the test."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpass")
        self.event = Event.objects.create(
            title="Test Event",
            start_date=datetime.now(),  # Provide a value for start_date
            # Provide a value for end_date if required
            end_date=datetime.now() + timedelta(days=1),
        )
        self.speaker = Speaker.objects.create(
            user_id=self.user,
            twitter="test_twitter",
            organization="Test Organization",
            bio="Test Bio",
            avatar="path/to/avatar.jpg",
        )
        self.talk = Talks.objects.create(
            event_id=self.event,
            title="Test Talk",
            description="Test Description",
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(hours=1),
        )
        self.talk.speaker_id.add(self.speaker)
        self.talk_url = reverse(
            "talk-retrieve-update-destroy", args=[self.talk.id])
        self.talk_list_url = reverse("talk-list-create")

    def test_list_talks(self):
        """Test the list of talks."""
        response = self.client.get(self.talk_list_url)
        talks = Talks.objects.all()
        serializer = TalkSerializer(talks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_talk(self):
        """Test the creation of a talk."""
        data = {
            "event_id": self.event.id,
            "title": "New Talk",
            "description": "New Description",
            "start_time": datetime.now(),
            "end_time": datetime.now() + timedelta(hours=1),
            "speaker_id": [self.speaker.id],
        }
        response = self.client.post(self.talk_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Talks.objects.count(), 2)
        self.assertEqual(Talks.objects.get(
            id=response.data["id"]).title, "New Talk")

    def test_retrieve_talk(self):
        """Test the retrieval of a talk."""
        response = self.client.get(self.talk_url)
        talk = Talks.objects.get(id=self.talk.id)
        serializer = TalkSerializer(talk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_talk(self):
        """Test the update of a talk."""
        data = {
            "title": "Updated Talk",
            "description": "Updated Description",
            "start_time": self.talk.start_time,
            "end_time": self.talk.end_time,
            "event_id": self.event.id,
            "speaker_id": [self.speaker.id],
        }
        response = self.client.put(self.talk_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.talk.refresh_from_db()
        self.assertEqual(self.talk.title, "Updated Talk")
        self.assertEqual(self.talk.description, "Updated Description")

    def test_delete_talk(self):
        """Test the deletion of a talk."""
        response = self.client.delete(self.talk_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Talks.objects.count(), 0)
