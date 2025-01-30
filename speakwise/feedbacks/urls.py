"""feedback urls."""

from django.urls import path
from . import views

app_name = "feedbacks"

urlpatterns = [
    path("", views.FeedbackListCreateView.as_view(), name="list_view"),
    path(
        "<int:pk>/",
        views.FeedbackDetailView.as_view(),
        name="detail_view",
    ),
]
