"""Authentication views for the Nebula app."""
import os
from abc import ABC
from abc import abstractmethod

from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from speakwise.authentication.models import PasswordReset

from speakwise.attendees.models import Attendee
from speakwise.attendees.serializers import AttendeeSerializer
from speakwise.speakers.models import SpeakerProfile
from speakwise.speakers.serializers import SpeakerSerializer
from speakwise.users.models import UserRole
from speakwise.authentication.serializers import ResetPasswordSerializer, ResetPasswordRequestSerializer
from .exceptions import AuthenticationError

User = get_user_model()

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
    """Login view for organizers."""

    def login(self):
        """Login the organizer."""
        self.user = self.serializer.validated_data["user"]
        if not self.user.role or self.user.role.display != "organizer":
            raise AuthenticationError
        return self.user


class AttendeeLoginView(LoginBaseClass):
    """Login view for attendees."""

    def login(self):
        """Login the attendee."""
        self.user = self.serializer.validated_data["user"]
        if not self.user.role or self.user.role.display != "attendee":
            raise AuthenticationError
        return self.user

    def get_extra_payload(self) -> dict:
        """Return the attendee data."""
        try:
            attendee = Attendee.objects.get(user=self.user)
        except Attendee.DoesNotExist as err:
            raise AuthenticationError from err
        serializer = AttendeeSerializer(attendee)
        return {"attendee": serializer.data}


class SpeakerLoginView(LoginBaseClass):
    """Login view for speaker."""

    def login(self):
        """Login the speaker."""
        self.user = self.serializer.validated_data["user"]
        if not self.user.role or self.user.role.display != "speaker":
            raise AuthenticationError
        return self.user

    def get_extra_payload(self) -> dict:
        """Return the speaker data."""
        try:
            admin = SpeakerProfile.objects.get(speaker_user=self.user)
        except SpeakerProfile.DoesNotExist as err:
            raise AuthenticationError from err
        serializer = SpeakerSerializer(admin)
        return {"speaker": serializer.data}

class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = []

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        new_password = data['new_password']
        confirm_password = data['confirm_password']
        
        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)
        
        reset_obj = PasswordReset.objects.filter(token=token).first()
        
        if not reset_obj:
            return Response({'error':'Invalid token'}, status=400)
        
        user = User.objects.filter(email=reset_obj.email).first()
        
        if user:
            user.set_password(request.data['new_password'])
            user.save()
            
            reset_obj.delete()
            
            return Response({'success':'Password updated'})
        else: 
            return Response({'error':'No user found'}, status=404)
        



class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        user = User.objects.filter(email__iexact=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user) 
            reset = PasswordReset(email=email, token=token)
            reset.save()

            reset_url = f"{os.environ['PASSWORD_RESET_BASE_URL']}/{token}"

            send_mail(
                subject="Password Reset Request",
                message=f"Click the link to reset your password: {reset_url}",
                from_email=os.environ['DEFAULT_FROM_EMAIL'],
                recipient_list=[email]
            )

            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with credentials not found"}, status=status.HTTP_404_NOT_FOUND)