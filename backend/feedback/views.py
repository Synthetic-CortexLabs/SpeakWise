from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Feedback
from .serializers import FeedbackSerializer


class ListCreateFeedbackView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer


class RetrieveUpdateDestroyFeedbackView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
