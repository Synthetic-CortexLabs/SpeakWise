"""API views for the users app."""

from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from speakwise.users.models import User

from .serializers import UserSerializer


class UserListView(APIView):
    """User list view."""

    def get_permissions(self):
        """Authentication is required to get the list of users."""
        if self.request.method == "GET":
            return [AllowAny()]
        return [AllowAny()]

    @extend_schema(
        description="Get the list of users.",
        responses={200: UserSerializer(many=True)},
    )
    def get(self, request):
        """Authentication (JWT) is required to get the list of users."""
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="Create a user.",
        request=UserSerializer,
        responses={201: UserSerializer},
    )
    def post(self, request):
        """Create a user."""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    """User detail view."""

    permission_classes = [AllowAny]

    def get_user(self, pk):
        """Get a user by pk."""
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description="Get a user by pk.",
        responses={200: UserSerializer},
    )
    def get(self, request, pk=None):
        """Get a user by pk."""
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(description="Update a user by pk.", responses={200: UserSerializer})
    def patch(self, request, pk=None):
        """Update a user by pk."""
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        """Delete a user by pk."""
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLoginView(APIView):
    """
    User login view.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        """
        Login a user.

        required fields: email, password

        """

        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            data={
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    """Logout a user."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Blacklist a refresh token requires a refresh token.

        Example:
            {'refresh_token': 'token'}
        """
        refresh_token = request.data["refresh_token"]
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
