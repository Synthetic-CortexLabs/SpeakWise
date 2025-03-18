"""API views for the users app."""

from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from speakwise.users.models import User

from .serializers import LoginSerializer
from .serializers import LogoutSerializer
from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    """User list view."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        operation_id="list_users",
        description="Get the list of users.",
        responses={200: UserSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="create_user",
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
    """View for retrieving and updating user details."""

    serializer_class = UserSerializer
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


class UserLoginView(generics.GenericAPIView):
    """User login view."""

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        operation_id="user_login",
        description="Login a user with email and password",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "user": {"$ref": "#/components/schemas/User"},
                    "refresh": {"type": "string"},
                    "access": {"type": "string"},
                },
            }
        },
    )
    def post(self, request):
        """Login a user."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data[
            "username"
        ]  # Using username field from LoginSerializer
        password = serializer.validated_data["password"]
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


class LogoutView(generics.GenericAPIView):
    """Logout a user."""

    serializer_class = LogoutSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        operation_id="user_logout",
        description="Blacklist a refresh token",
        responses={204: None},
    )
    def post(self, request):
        """Blacklist a refresh token."""
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except refresh_token.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
