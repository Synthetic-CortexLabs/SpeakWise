"""authentication urls module."""

from django.urls import path

from speakwise.authentication import views

app_name = "authentication"

urlpatterns = [
    path("auth/attendee/", views.AttendeeLoginView.as_view(), name="attendee-auth"),
    path("auth/organizer/", views.OrganizerLoginView.as_view(), name="organizer-auth"),
    path("auth/speaker/", views.SpeakerLoginView.as_view(), name="speaker-auth"),
    path('auth/reset-password/', views.RequestPasswordReset.as_view(), name='reset-password'),
    path('auth/reset-password-confirm/', views.ResetPassword.as_view(), name='reset-password-confirm'),
]
