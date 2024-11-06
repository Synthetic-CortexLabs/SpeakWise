# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from feedbacks.models import Feedback
from feedbacks.serializers import FeedbackSerializer

class FeedbackListCreateView(generics.ListCreateAPIView):
    """
    List all feedbacks, or create a new feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)


class RetrieveUpdateDestroyFeedbackView(generics.RetrieveUpdateDestroyView):
    """
    Retrieve, update or delete a feedback instance.
    """

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)




