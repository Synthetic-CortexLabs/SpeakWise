"""attendees urls."""

from django.urls import path

from speakwise.attendees.views import AttendeeByEmailView
from speakwise.attendees.views import AttendeeDetailView
from speakwise.attendees.views import AttendeeListCreateView
from speakwise.attendees.views import ValidateAttendeeView

app_name = "attendees"

urlpatterns = [
    path("", AttendeeListCreateView.as_view(), name="list_view"),
    path("<int:pk>/", AttendeeDetailView.as_view(), name="detail_view"),
    path(
        "by-email/<str:email>/",
        AttendeeByEmailView.as_view(),
        name="by-email",
    ),
    path(
        "verify-attendee/",
        ValidateAttendeeView.as_view(),
        name="verify-attendee",
    ),
]
