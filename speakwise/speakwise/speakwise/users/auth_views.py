# views.py
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from .serializers import UserSerializer

@extend_schema(request=UserSerializer, responses={200: UserSerializer})
class RegisterView(APIView):
    """
    RegisterView handles user registration.
    This view allows any user to register by providing the necessary data.
    It validates the provided data using UserSerializer and, if valid, creates a new user.
    Upon successful registration, it generates and returns JWT tokens (refresh and access) along with the user data.
    Methods:
        post(request): Handles the POST request to register a new user.
            - request: The HTTP request containing user registration data.
            - Returns: A Response object with user data and JWT tokens if registration is successful,
                       or error details if registration fails.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
