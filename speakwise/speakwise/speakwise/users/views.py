"""user views."""

from django.contrib.auth import authenticate
from django.http import Http404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from speakwise.users.models import User
from speakwise.users.serializers import UserSerializer


class UserList(APIView):
    """Handle user listing and creation.

    This view allows any user to list all users and create a new user.
    It provides a list of all users and allows creating a new user.

    Methods:
        get(request): Handle user listing GET request.
            Args:
                request: HTTP request.
            Returns:
                Response with a list of all users.
        post(request): Handle user creation POST request.
            Args:
                request: HTTP request with user data.
            Returns:
                Response with the created user data or error details.
    """

    permission_classes = (AllowAny,)

    @extend_schema(responses={200: UserSerializer(many=True)})
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @extend_schema(request=UserSerializer, responses={201: UserSerializer, 400: None})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    """user detail view."""

    permission_classes = (AllowAny,)

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist as error:
            raise Http404 from error

    def get(self, request, pk=None):
        """get a user."""
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, pk=None):
        """update a user."""
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        """delete a user."""
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthenticateUser(APIView):
    """login user and return user data with tokens."""

    permission_classes = (AllowAny,)

    def post(self, request):
        """login user and return user data with tokens."""
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            return Response(
                {
                    "user": serializer.data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    """Logout user."""

    permission_classes = (AllowAny,)

    def post(self, request):
        """Logout user."""
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            raise Http404 from error
