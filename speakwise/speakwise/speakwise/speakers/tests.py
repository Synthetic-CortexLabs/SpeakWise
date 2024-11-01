"""Speakers app tests."""

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Speaker
from .serializers import SpeakerSerializer

User = get_user_model()


class SpeakerModelTest(TestCase):
    """Test speaker model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.speaker = Speaker.objects.create(
            user_id=self.user,
            twitter="test_twitter",
            organization="Test Organization",
            bio="This is a test bio",
            avatar="path/to/avatar.jpg",
        )

    def test_str_method(self):
        """Test string representation of the speaker."""
        self.assertEqual(str(self.speaker), "testuser")

    def test_get_absolute_url(self):
        """Test get absolute URL method."""
        url = self.speaker.get_absolute_url()
        self.assertEqual(url, f"/speakers/{self.speaker.pk}/")


class SpeakerSerializerTest(TestCase):
    """Test speaker serializer."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.speaker_data = {
            "user_id": self.user,
            "twitter": "test_twitter",
            "organization": "Test Organization",
            "bio": "This is a test bio",
        }
        self.speaker = Speaker.objects.create(**self.speaker_data)
        self.serializer = SpeakerSerializer(instance=self.speaker)

    def test_contains_expected_fields(self):
        """Test that the serializer contains the expected fields."""
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            [
                "user_id",
                "twitter",
                "organization",
                "avatar",
                "bio",
                "id",
                "created_at",
                "updated_at",
            ],
        )

    def test_field_content(self):
        """Test that the serializer returns the expected content."""
        data = self.serializer.data
        self.assertEqual(data["user_id"], self.user.id)
        self.assertEqual(data["twitter"], "test_twitter")
        self.assertEqual(data["organization"], "Test Organization")
        self.assertEqual(data["bio"], "This is a test bio")


class SpeakerAPITest(APITestCase):
    """Test speaker API."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.user2 = User.objects.create_user(
            username="testsuser", password="password123"
        )
        self.client.login(username="testuser", password="password123")
        self.speaker = Speaker.objects.create(
            user_id=self.user,
            twitter="test_twitter",
            organization="Test Organization",
            bio="This is a test bio",
            avatar="path/to/avatar.jpg",
        )
        self.list_create_url = reverse("list_create_speakers")
        self.detail_url = reverse("speaker_detail", kwargs={"pk": self.speaker.pk})

    def test_create_speaker(self):
        """Test creating a new speaker."""
        data = {
            "user_id": self.user2.id,
            "twitter": "new_twitter",
            "organization": "New Organization",
            "bio": "This is another test bio",
        }
        response = self.client.post(self.list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Speaker.objects.count(), 2)

    def test_list_speakers(self):
        """Test listing all speakers."""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Speaker.objects.count())

    def test_retrieve_speaker(self):
        """Test retrieving a speaker."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["twitter"], self.speaker.twitter)

    def test_update_speaker(self):
        """Test updating a speaker."""
        data = {"twitter": "updated_twitter"}
        response = self.client.patch(self.detail_url, data)
        self.speaker.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.speaker.twitter, "updated_twitter")

    def test_delete_speaker(self):
        """Test deleting a speaker."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Speaker.objects.count(), 0)
