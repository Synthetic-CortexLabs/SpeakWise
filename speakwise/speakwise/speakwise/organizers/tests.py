# tests/test_organizers.py
from django.urls import reverse
from rest_framework.test import APITestCase

from speakwise.events.models import Event
from speakwise.users.models import User

from .models import Organizers
from .models import SocialLinks


class OrganizerTests(APITestCase):
    def setUp(self):
        """Set up test data"""
        # Create test user with email authentication
        self.user = User.objects.create_user(
            email="test@example.com",
            password="",
        )

        # Create test social links
        self.social = SocialLinks.objects.create(
            social_name="Twitter",
            social_link="https://twitter.com/test",
        )

        # Create test event
        self.event = Event.objects.create(
            name="Test Event",
            description="Test Description",
        )

        # Create test organizer
        self.organizer = Organizers.objects.create(
            user_id=self.user,
            organization="Test Org",
            socials=self.social,
            events=self.event,
        )

        # Login with email instead of username
        self.client.login(email="test@example.com", password="")

        # URLs for testing
        self.list_url = reverse("organizers:organizer-list-create")
        self.detail_url = reverse(
            "organizers:organizer-detail",
            kwargs={"pk": self.organizer.pk},
        )
