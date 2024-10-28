from django.urls import path
from .views import SpeakerListCreateView, RetrieveUpdateDestroySpeakerView


urlpatterns = [
    path("", SpeakerListCreateView.as_view(), name="list_create_speakers"),
    path("<int:pk>/", RetrieveUpdateDestroySpeakerView.as_view(), name="speaker_detail"),
]
