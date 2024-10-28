from django.urls import path
from feedback.views import ListCreateFeedbackView, RetrieveUpdateDestroyFeedbackView


app_name = "feedback"
urlpatterns = [
    path('feedback/', ListCreateFeedbackView, name='list_feedback'),
    path('feedback/<str:pk>/', RetrieveUpdateDestroyFeedbackView, name='feedback_detail'),
]
