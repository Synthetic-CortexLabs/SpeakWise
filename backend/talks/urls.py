"""Talks urls configuration module."""

from django.urls import path
from talks.views import TalkListCreateView, TalkRetrieveUpdateDestroyView

urlpatterns = [
    path("talks/", TalkListCreateView.as_view(), name="talk-list-create"),
    path(
        "talks/<int:pk>/",
        TalkRetrieveUpdateDestroyView.as_view(),
        name="talk-retrieve-update-destroy",
    ),
]
