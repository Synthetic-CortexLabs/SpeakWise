"""Talks urls configuration module."""

from django.urls import path

from speakwise.talks.views import TalkListCreateView
from speakwise.talks.views import TalkRetrieveUpdateDestroyView

app_name = "talks"

urlpatterns = [
    path("talks/", TalkListCreateView.as_view(), name="talk-list-create"),
    path(
        "talks/<int:pk>/",
        TalkRetrieveUpdateDestroyView.as_view(),
        name="talk-retrieve-update-destroy",
    ),
]
