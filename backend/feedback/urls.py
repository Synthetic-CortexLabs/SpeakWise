from django.urls import path
from feedback.views import (
    ListCreateFeedbackView,
    RetrieveUpdateDestroyFeedbackView,
)


app_name = "feedback"
urlpatterns = [
    path("feedback/", ListCreateFeedbackView.as_view(), name="list_feedback"),
    path(
        "feedback/<str:pk>/",
        RetrieveUpdateDestroyFeedbackView.as_view(),
        name="feedback_detail",
    ),
]
