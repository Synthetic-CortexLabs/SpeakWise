"""authentication urls module."""

from django.urls import path

from . import views

app_name = "authentication"

urlpatterns = [
    path("auth/attendee/", views.AttendeeLoginView.as_view(), name="attendee-auth"),
    path("auth/organizer/", views.OrganizerLoginView.as_view(), name="organizer-auth"),
    path("auth/speaker/", views.SpeakerLoginView.as_view(), name="speaker-auth"),
]
