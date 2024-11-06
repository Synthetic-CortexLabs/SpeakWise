from django.urls import path
from feedbacks.views import FeedbackListCreateView, RetrieveUpdateDestroyFeedbackView

urlpatterns = [
    path("feedbacks/", FeedbackListCreateView.as_view(), name="feedback-list-create"),
    path("feedbacks/<int:pk>/", RetrieveUpdateDestroyFeedbackView.as_view(), name="feedback-retrieve-update-destroy"),
]
