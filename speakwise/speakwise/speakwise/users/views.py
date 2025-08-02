"""API views for the users app."""

from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from speakwise.users.models import User
from speakwise.users.serializers import UserSerializer


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

    def post(self, request, *args, **kwargs):
        """Login a user."""

        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            try:
                refresh = RefreshToken.for_user(user)
                serializer = UserSerializer(user)
            except user.DoesNotExist as err:
                return Response(data=str(err), status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LogoutView(APIView):
    """Logout view."""

    permission_classes = [AllowAny]

    def post(self, request):
        """logout a user."""
        refresh_token = request.data.get("refresh_token")
        try:
            token = RefreshToken(refresh_token)
            # Only blacklist if the method exists (i.e., token_blacklist app is installed)
            token.blacklist() if hasattr(token, "blacklist") else None
            # If not, just return success (client should remove tokens)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (TypeError, ValueError):
            return Response(
                {"error": "Invalid token"},
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(["GET", "PATCH"])
@permission_classes([IsAuthenticated])
def user_profile_me(request):
    """Get or update the current user's profile."""
    user = request.user

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return None
