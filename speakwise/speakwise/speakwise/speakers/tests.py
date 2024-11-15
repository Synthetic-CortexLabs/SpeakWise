"""Speakers app tests."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Speaker
from .serializers import SpeakerSerializer

User = get_user_model()


class SpeakerModelTest(TestCase):
    """Test speaker model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            name="testuser",
            password="password123",
            email="example@mail.com",
        )
        self.speaker = Speaker.objects.create(
            user_id=self.user.pk,
            twitter="test_twitter",
            organization="Test Organization",
            bio="This is a test bio",
            avatar="path/to/avatar.jpg",
        )

    def test_str_method(self):
        """Test string representation of the speaker."""
        self.assertEqual(str(self.speaker.user.name), "testuser")


class SpeakerSerializerTest(TestCase):
    """Test speaker serializer."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            name="testuser",
            password="password123",
            email="user@mail.com",
        )
        self.speaker_data = {
            "user_id": self.user.pk,
            "twitter": "test_twitter",
            "organization": "Test Organization",
            "bio": "This is a test bio",
        }
        self.speaker = Speaker.objects.create(**self.speaker_data)
        self.serializer = SpeakerSerializer(instance=self.speaker)

    def test_contains_expected_fields(self):
        """Test that the serializer contains the expected fields."""
        data = self.serializer.data
        objects = ["user_id", "twitter", "organization", "bio"]
        assert [i in data for i in objects]

    def test_field_content(self):
        """Test that the serializer returns the expected content."""
        data = self.serializer.data
        assert data["id"] == self.speaker.pk
        assert data["twitter"] == "test_twitter"
        assert data["organization"] == "Test Organization"
        assert data["bio"] == "This is a test bio"


class SpeakerAPITest(APITestCase):
    """Test speaker API."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            name="testuser",
            password="password123",
            email="example@mail.com",
        )
        self.user2 = User.objects.create_user(
            name="testsuser",
            password="password123",
            email="example1@mail.com",
        )
        self.speaker = Speaker.objects.create(
            user_id=self.user.pk,
            twitter="test_twitter",
            organization="Test Organization",
            bio="This is a test bio",
            avatar="path/to/avatar.jpg",
        )
        self.list_create_url = reverse("speakers:list_create_speakers")
        self.detail_url = reverse(
            "speakers:speaker_detail",
            kwargs={"pk": self.speaker.pk},
        )

    def test_create_speaker(self):
        """Test creating a new speaker."""
        data = {
            "user_id": self.user2.id,
            "twitter": "new_twitter",
            "organization": "New Organization",
            "bio": "This is another test bio",
            "user": self.user2.pk,
        }
        self.client.force_login(self.user)

        response = self.client.post(self.list_create_url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Speaker.objects.count() == 2

    def test_list_speakers(self):
        """Test listing all speakers."""
        self.client.force_login(self.user)

        response = self.client.get(self.list_create_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == Speaker.objects.count()

    def test_retrieve_speaker(self):
        """Test retrieving a speaker."""
        self.client.force_login(self.user)

        response = self.client.get(
            self.detail_url,
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["twitter"] == self.speaker.twitter

    def test_update_speaker(self):
        """Test updating a speaker."""
        self.client.force_login(self.user)

        data = {"twitter": "updated_twitter"}
        response = self.client.patch(self.detail_url, data)

        self.speaker.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert self.speaker.twitter == "updated_twitter"

    def test_delete_speaker(self):
        """Test deleting a speaker."""
        self.client.force_login(self.user)

        response = self.client.delete(self.detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Speaker.objects.count() == 0
