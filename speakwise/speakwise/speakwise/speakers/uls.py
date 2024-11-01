"""Speakers URLs."""

from django.urls import path

from .views import RetrieveUpdateDestroySpeakerView
from .views import SpeakerListCreateView

urlpatterns = [
    path("", SpeakerListCreateView.as_view(), name="list_create_speakers"),
    path(
        "<int:pk>/", RetrieveUpdateDestroySpeakerView.as_view(), name="speaker_detail"
    ),
]
