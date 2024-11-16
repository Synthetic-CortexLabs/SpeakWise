from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from speakwise.users.serializers import UserSerializer


@extend_schema(
    tags=["Authentication"],
    description="Register a new user",
    request=UserSerializer,
    responses={201: UserSerializer, 400: None},
)
class RegisterView(generics.CreateAPIView):
    """Handle user registration with JWT token generation.

    This view allows any user to register by providing the necessary data.
    It validates the provided data using UserSerializer and creates a new user
    if valid.

    Upon successful registration, it returns:
        - User data
        - JWT refresh token
        - JWT access token

    Methods:
        post(request): Handle user registration POST request.
            Args:
                request: HTTP request with registration data.
            Returns:
                Response with user data and tokens, or error details.
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            refresh = RefreshToken.for_user(serializer)
            return Response(
                {
                    "user": serializer.data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
