"""attendees urls."""

from django.urls import path

from speakwise.attendees.views import AttendeeDetailView
from speakwise.attendees.views import AttendeeListCreateView

app_name = "attendees"

urlpatterns = [
    path("", AttendeeListCreateView.as_view(), name="list_view"),
    path("<int:pk>/", AttendeeDetailView.as_view(), name="detail_view"),
]
