"""Tests for authentication permissions."""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from speakwise.attendees.models import Attendee
from speakwise.events.models import Event
from speakwise.events.models import Session
from speakwise.feedbacks.models import Feedback
from speakwise.speakers.models import SpeakerProfile
from speakwise.users.choices import UserRoles
from speakwise.users.models import User
from speakwise.users.models import UserRole


class PermissionsTestCase(TestCase):
    """Test case for role-based access control permissions."""

    def setUp(self):
        """Set up test data."""
        # Create user roles
        self.attendee_role = UserRole.objects.create(display=UserRoles.ATTENDEE)
        self.speaker_role = UserRole.objects.create(display=UserRoles.SPEAKER)
        self.organizer_role = UserRole.objects.create(display=UserRoles.ORGANIZER)
        self.admin_role = UserRole.objects.create(display=UserRoles.ADMIN)

        # Create users with different roles
        self.attendee_user = User.objects.create_user(
            email="attendee@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="Attendee",
            nationality="Test Country",
            role=self.attendee_role,
        )

        self.speaker_user = User.objects.create_user(
            email="speaker@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="Speaker",
            nationality="Test Country",
            role=self.speaker_role,
        )

        self.organizer_user = User.objects.create_user(
            email="organizer@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="Organizer",
            nationality="Test Country",
            role=self.organizer_role,
        )

        self.admin_user = User.objects.create_user(
            email="admin@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="Admin",
            nationality="Test Country",
            role=self.admin_role,
        )

        # Create speaker profile
        self.speaker_profile = SpeakerProfile.objects.create(
            user=self.speaker_user,
            bio="Test speaker bio",
            profile_picture="test.jpg",
        )

        # Create attendee profile
        self.attendee = Attendee.objects.create(
            user=self.attendee_user,
            phone_number="1234567890",
        )

        # Create an event
        self.event = Event.objects.create(
            name="Test Event",
            description="Test event description",
            start_date="2025-06-01",
            end_date="2025-06-05",
            location="Test Location",
        )

        # Create a session
        self.session = Session.objects.create(
            title="Test Session",
            description="Test session description",
            start_time="10:00:00",
            end_time="11:00:00",
            event=self.event,
            speaker=self.speaker_profile,
        )

        # Create feedback
        self.feedback = Feedback.objects.create(
            attendee=self.attendee,
            session=self.session,
            rating=5,
            comment="Great session!",
        )

        # API clients with different authentications
        self.anonymous_client = APIClient()

        self.attendee_client = APIClient()
        self.attendee_client.force_authenticate(user=self.attendee_user)

        self.speaker_client = APIClient()
        self.speaker_client.force_authenticate(user=self.speaker_user)

        self.organizer_client = APIClient()
        self.organizer_client.force_authenticate(user=self.organizer_user)

        self.admin_client = APIClient()
        self.admin_client.force_authenticate(user=self.admin_user)

    def test_session_list_access(self):
        """Test that all users can list sessions."""
        url = reverse("api:session-list")

        # Anonymous users can view sessions
        response = self.anonymous_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Attendees can view sessions
        response = self.attendee_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Speakers can view sessions
        response = self.speaker_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Organizers can view sessions
        response = self.organizer_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Admins can view sessions
        response = self.admin_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_session_create_permissions(self):
        """Test that only organizers and admins can create sessions."""
        url = reverse("api:session-list")
        data = {
            "title": "New Session",
            "description": "New session description",
            "start_time": "09:00:00",
            "end_time": "10:00:00",
            "event": self.event.id,
            "speaker": self.speaker_profile.id,
        }

        # Anonymous users cannot create sessions
        response = self.anonymous_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Attendees cannot create sessions
        response = self.attendee_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Speakers cannot create sessions
        response = self.speaker_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Organizers can create sessions
        response = self.organizer_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Admins can create sessions
        data["title"] = "Another New Session"
        response = self.admin_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_session_update_permissions(self):
        """Test session update permissions."""
        url = reverse("api:session-detail", kwargs={"pk": self.session.id})
        data = {"title": "Updated Session Title"}

        # Anonymous users cannot update sessions
        response = self.anonymous_client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Attendees cannot update sessions
        response = self.attendee_client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Speakers can update their own sessions
        response = self.speaker_client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Organizers can update any session
        data["title"] = "Organizer Updated Title"
        response = self.organizer_client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Admins can update any session
        data["title"] = "Admin Updated Title"
        response = self.admin_client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_feedback_permissions(self):
        """Test feedback permissions."""
        list_url = reverse("api:feedback-list")
        detail_url = reverse("api:feedback-detail", kwargs={"pk": self.feedback.id})

        # Test GET list permissions
        self.assertEqual(
            self.anonymous_client.get(list_url).status_code,
            status.HTTP_401_UNAUTHORIZED,
        )
        self.assertEqual(
            self.attendee_client.get(list_url).status_code,
            status.HTTP_403_FORBIDDEN,
        )
        self.assertEqual(
            self.speaker_client.get(list_url).status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            self.organizer_client.get(list_url).status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            self.admin_client.get(list_url).status_code,
            status.HTTP_200_OK,
        )

        # Test POST permissions
        data = {
            "attendee": self.attendee.id,
            "session": self.session.id,
            "rating": 4,
            "comment": "Good session",
        }
        self.assertEqual(
            self.anonymous_client.post(list_url, data).status_code,
            status.HTTP_401_UNAUTHORIZED,
        )
        self.assertEqual(
            self.attendee_client.post(list_url, data).status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            self.speaker_client.post(list_url, data).status_code,
            status.HTTP_403_FORBIDDEN,
        )

        # Test GET detail permissions
        self.assertEqual(
            self.anonymous_client.get(detail_url).status_code,
            status.HTTP_401_UNAUTHORIZED,
        )
        self.assertEqual(
            self.attendee_client.get(detail_url).status_code,
            status.HTTP_403_FORBIDDEN,
        )
        self.assertEqual(
            self.speaker_client.get(detail_url).status_code,
            status.HTTP_200_OK,
        )

        # Test PATCH permissions
        data = {"rating": 3, "comment": "Average session"}
        self.assertEqual(
            self.anonymous_client.patch(detail_url, data).status_code,
            status.HTTP_401_UNAUTHORIZED,
        )
        self.assertEqual(
            self.attendee_client.patch(detail_url, data).status_code,
            status.HTTP_403_FORBIDDEN,
        )
        self.assertEqual(
            self.speaker_client.patch(detail_url, data).status_code,
            status.HTTP_200_OK,
        )

        # Test DELETE permissions
        new_feedback = Feedback.objects.create(
            attendee=self.attendee,
            session=self.session,
            rating=2,
            comment="Not great",
        )
        delete_url = reverse("api:feedback-detail", kwargs={"pk": new_feedback.id})
        self.assertEqual(
            self.attendee_client.delete(delete_url).status_code,
            status.HTTP_403_FORBIDDEN,
        )
        self.assertEqual(
            self.speaker_client.delete(delete_url).status_code,
            status.HTTP_200_OK,
        )


class AuthenticationTestCase(TestCase):
    """Test case for authentication views."""

    def setUp(self):
        """Set up test data."""
        # Create user roles
        self.attendee_role = UserRole.objects.create(display=UserRoles.ATTENDEE)
        self.speaker_role = UserRole.objects.create(display=UserRoles.SPEAKER)
        self.organizer_role = UserRole.objects.create(display=UserRoles.ORGANIZER)

        # Create users with different roles
        self.attendee_user = User.objects.create_user(
            email="attendee@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="Attendee",
            nationality="Test Country",
            role=self.attendee_role,
        )

        self.speaker_user = User.objects.create_user(
            email="speaker@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="Speaker",
            nationality="Test Country",
            role=self.speaker_role,
        )

        self.organizer_user = User.objects.create_user(
            email="organizer@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="Organizer",
            nationality="Test Country",
            role=self.organizer_role,
        )

        # Create wrong role user (speaker with attendee role)
        self.wrong_role_user = User.objects.create_user(
            email="wrong@example.com",
            password="testpassword123",
            first_name="Wrong",
            last_name="Role",
            nationality="Test Country",
            role=self.attendee_role,
        )

        # Create speaker profile
        self.speaker_profile = SpeakerProfile.objects.create(
            user=self.speaker_user,
            bio="Test speaker bio",
            profile_picture="test.jpg",
        )

        # Create attendee profile
        self.attendee = Attendee.objects.create(
            user=self.attendee_user,
            phone_number="1234567890",
        )

        # API client
        self.client = APIClient()

    def test_attendee_login(self):
        """Test attendee login view."""
        url = reverse("authentication:attendee-auth")

        # Successful login
        response = self.client.post(
            url,
            {
                "email": "attendee@example.com",
                "password": "testpassword123",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

        # Wrong password
        response = self.client.post(
            url,
            {
                "email": "attendee@example.com",
                "password": "wrongpassword",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Wrong role (speaker trying to use attendee login)
        response = self.client.post(
            url,
            {
                "email": "speaker@example.com",
                "password": "testpassword123",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_speaker_login(self):
        """Test speaker login view."""
        url = reverse("authentication:speaker-auth")

        # Successful login
        response = self.client.post(
            url,
            {
                "email": "speaker@example.com",
                "password": "testpassword123",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("speaker", response.data)

        # Wrong role (attendee trying to use speaker login)
        response = self.client.post(
            url,
            {
                "email": "attendee@example.com",
                "password": "testpassword123",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_organizer_login(self):
        """Test organizer login view."""
        url = reverse("authentication:organizer-auth")

        # Successful login
        response = self.client.post(
            url,
            {
                "email": "organizer@example.com",
                "password": "testpassword123",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

        # Wrong role (attendee trying to use organizer login)
        response = self.client.post(
            url,
            {
                "email": "attendee@example.com",
                "password": "testpassword123",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
