from rest_framework.generics import CreateAPIView
from rest_framework.response import Response 
from rest_framework.permissions import  AllowAny
from rest_framework import status
from .models import User
from .auth_serializers import UserRegistrationSerializer

class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the new user using the serializer's create method
        user = serializer.save()

        # Customize the response
        return Response(
            {
                "message": "User registered successfully",
                "user_id": user.id,
                "role": serializer.data["role"],
                "email": user.email
            },
            status=status.HTTP_201_CREATED
        )

