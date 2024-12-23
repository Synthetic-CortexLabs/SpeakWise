"""Authentication views for the Nebula app."""

from abc import ABC
from abc import abstractmethod

from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from speakwise.attendees.models import Attendee
from speakwise.attendees.serializers import AttendeeSerializer
from speakwise.organizers.models import Organizers
from speakwise.organizers.serializers import OrganizerSerializer
from speakwise.speakers.models import Speaker
from speakwise.speakers.serializers import SpeakerSerializer
from speakwise.users.models import UserRole

from .exceptions import AuthenticationError


class LoginBaseClass(ABC, LoginView):
    """This class inherits the LoginView from the rest_auth package.
    Django rest auth lib does not support the refresh token
    logic. However,restframework_simplejwt does. Rest auth was
    used because it's based off all-auth which can be used for
    social logins as well as signing in with either username or
    password(of which simplejwt does not support). The two libraries
    were combined to give the required results.
    """

    def get_extra_payload(self) -> dict:
        """This method is used to add extra payload to the refresh token."""
        return {}

    def get_token(self, user):
        """Generate the refresh token."""
        refresh_token = RefreshToken.for_user(user)
        for key, value in self.get_extra_payload().items():
            refresh_token[key] = value
        return refresh_token

    @abstractmethod
    def login(self):
        """Login in the user."""

    def get_response(self):
        """Return the response with the refresh token."""
        data = {}

        refresh = self.get_token(self.user)
        # generate access and refresh tokens
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return Response(data)


class OrganizerLoginView(LoginBaseClass):
    """Login view for practitioners."""

    def login(self):
        """Login the organizer."""
        try:
            self.user = self.serializer.validated_data["user"]
            # check if user has practitioner among its UserRoles
            self.user.role.get(display="organizer")
            return self.user
        except UserRole.DoesNotExist as err:
            raise AuthenticationError from err

    def get_extra_payload(self) -> dict:
        """Return the organizer data."""
        practitioner = Organizers.objects.get(user=self.user)
        serializer = OrganizerSerializer(practitioner)
        return {"practitioner": serializer.data}


class AttendeeLoginView(LoginBaseClass):
    """Login view for patients."""

    def login(self):
        """Login the attendee."""
        try:
            self.user = self.serializer.validated_data["user"]
            print(self.user.role.display)
            # self.user.role.get(display="attendee")
            self.user.role.display = "attendee"
            return self.user
        except UserRole.DoesNotExist as err:
            raise AuthenticationError from err

    def get_extra_payload(self) -> dict:
        """Return the attendee data."""
        practitioner = Attendee.objects.get(user=self.user)
        serializer = AttendeeSerializer(practitioner)
        return {"attendee": serializer.data}


class SpeakerLoginView(LoginBaseClass):
    """Login view for speaker."""

    def login(self):
        """Login the speaker."""
        try:
            self.user = self.serializer.validated_data["user"]
            self.user.role.get(display="speaker")
            return self.user
        except UserRole.DoesNotExist as err:
            raise AuthenticationError from err

    def get_extra_payload(self) -> dict:
        """Return the speaker data."""
        admin = Speaker.objects.get(user=self.user)
        serializer = SpeakerSerializer(admin)
        return {"speaker": serializer.data}
