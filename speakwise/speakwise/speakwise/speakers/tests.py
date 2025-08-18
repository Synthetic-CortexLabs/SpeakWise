import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from speakwise.events.models import Event
from speakwise.feedbacks.models import Feedback

from .models import SkillTag
from .models import SpeakerDashboard
from .models import SpeakerProfile
from .models import SpeakerSocialLink
from .serializers import SkillTagSerializer
from .serializers import SpeakerProfileSerializer

User = get_user_model()


class SkillTagTests(TestCase):
    """Test suite for SkillTag model."""

    def setUp(self):
        self.skill_tag = SkillTag.objects.create(name="Python")

    def test_skill_tag_creation(self):
        assert str(self.skill_tag) == "Python"
        assert isinstance(self.skill_tag, SkillTag)

    def test_unique_constraint(self):
        with pytest.raises(Exception):  # noqa: B017, PT011
            SkillTag.objects.create(name="Python")


class SpeakerProfileTests(TestCase):
    """Test suite for SpeakerProfile model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="speaker1",
            email="speaker1@test.com",
            password="testpass123",
        )
        self.profile = SpeakerProfile.objects.create(
            speaker_user=self.user,
            organization="Test Org",
            short_bio="Test Bio",
            long_bio="Detailed Bio",
            country="Test Country",
        )
        self.skill_tag = SkillTag.objects.create(name="Python")

    def test_profile_creation(self):
        assert str(self.profile) == self.user.get_full_name()

    def test_add_skill_tags(self):
        self.profile.skill_tags.add(self.skill_tag)
        assert self.profile.skill_tags.count() == 1

    def test_avatar_upload(self):
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",
            content_type="image/jpeg",
        )
        self.profile.avatar = image
        self.profile.save()
        assert self.profile.avatar


class SpeakerDashboardTests(TestCase):
    """Test suite for SpeakerDashboard functionality."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="speaker1",
            email="speaker1@test.com",
            password="testpass123",
        )
        self.profile = SpeakerProfile.objects.create(
            speaker_user=self.user,
            organization="Test Org",
        )
        self.event = Event.objects.create(
            name="Test Event",
            date="2024-03-20",
        )
        self.profile.events_spoken.add(self.event)
        self.feedback = Feedback.objects.create(
            speaker=self.profile,
            event=self.event,
            rating=4.5,
        )
        self.dashboard = SpeakerDashboard.objects.create(
            speaker_profile=self.profile,
            feedback=self.feedback,
        )

    def test_feedback_calculations(self):
        assert self.dashboard.total_events == 1
        assert self.dashboard.average_feedback_rating == 4.5

    def test_feedback_per_conference(self):
        conference_ratings = self.dashboard.feedback_rate_per_conference
        assert isinstance(conference_ratings, dict)


class APITests(APITestCase):
    """Test suite for API endpoints."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.client.force_authenticate(user=self.user)
        self.profile = SpeakerProfile.objects.create(
            speaker_user=self.user,
            organization="Test Org",
        )
        self.skill_tag = SkillTag.objects.create(name="Python")

    def test_speaker_profile_list(self):
        url = reverse("speaker-profile-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_speaker_profile_create(self):
        url = reverse("speaker-profile-create")
        data = {
            "organization": "New Org",
            "short_bio": "New Bio",
            "country": "New Country",
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_speaker_profile_update(self):
        url = reverse("speaker-profile-detail", kwargs={"pk": self.profile.pk})
        data = {"organization": "Updated Org"}
        response = self.client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["organization"] == "Updated Org"


class SerializerTests(TestCase):
    """Test suite for serializers."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.profile = SpeakerProfile.objects.create(
            speaker_user=self.user,
            organization="Test Org",
        )
        self.skill_tag = SkillTag.objects.create(name="Python")
        self.profile.skill_tags.add(self.skill_tag)

    def test_speaker_profile_serializer(self):
        serializer = SpeakerProfileSerializer(self.profile)
        assert "skill_tags" in serializer.data
        assert "social_links" in serializer.data
        assert "full_name" in serializer.data

    def test_skill_tag_serializer(self):
        serializer = SkillTagSerializer(self.skill_tag)
        assert serializer.data["name"] == "Python"


class SpeakerSocialLinkTests(TestCase):
    """Test suite for SpeakerSocialLink model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testspeaker",
            email="speaker@test.com",
            password="testpass123",
        )
        self.profile = SpeakerProfile.objects.create(
            speaker_user=self.user,
            organization="Test Org",
            short_bio="Test Bio",
        )
        self.social_link = SpeakerSocialLink.objects.create(
            speaker=self.profile,
            social_name="Twitter",
            social_url="https://twitter.com/testuser",
            display_order=1,
        )

    def test_social_link_creation(self):
        """Test basic social link creation."""
        assert self.social_link.social_name == "Twitter"
        assert self.social_link.social_url == "https://twitter.com/testuser"
        assert self.social_link.is_active
        assert self.social_link.display_order == 1

    def test_string_representation(self):
        """Test string representation of social link."""
        expected = f"{self.profile}'s Twitter link"
        assert str(self.social_link) == expected

    def test_unique_constraint(self):
        """Test unique constraint for speaker and social_name."""
        with pytest.raises(ValidationError):  # noqa: PT012
            duplicate = SpeakerSocialLink(
                speaker=self.profile,
                social_name="Twitter",
                social_url="https://twitter.com/another",
            )
            duplicate.full_clean()
            duplicate.save()

    def test_ordering(self):
        """Test social links ordering."""
        second_link = SpeakerSocialLink.objects.create(
            speaker=self.profile,
            social_name="LinkedIn",
            social_url="https://linkedin.com/testuser",
            display_order=0,
        )
        links = SpeakerSocialLink.objects.all()
        assert links[0] == second_link  # Lower display_order comes first

    def test_related_name_access(self):
        """Test accessing social links through speaker profile."""
        assert self.profile.social_links.count() == 1
        assert self.profile.social_links.first() == self.social_link
