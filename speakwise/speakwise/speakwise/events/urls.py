from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from speakwise.events import views

app_name = "events"

urlpatterns = [
    # Events
    path("", views.EventListCreateAPIView.as_view(), name="event-list-create"),
    path(
        "<int:pk>/",
        views.EventRetrieveUpdateDestroyAPIView.as_view(),
        name="event-retrieve-update-destroy",
    ),
    # Tags
    path(
        "tags/",
        views.TagListCreateAPIView.as_view(),
        name="tag-list-create",
    ),
    path(
        "tags/<int:pk>/",
        views.TagRetrieveUpdateDestroyAPIView.as_view(),
        name="tag-retrieve-update-destroy",
    ),
    # Countries
    path(
        "countries/",
        views.CountryListCreateAPIView.as_view(),
        name="country-list-create",
    ),
    path(
        "countries/<int:pk>/",
        views.CountryRetrieveUpdateDestroyAPIView.as_view(),
        name="country-retrieve-update-destroy",
    ),

    # Sessions
    path(
        "sessions/",
        views.SessionListCreateAPIView.as_view(),
        name="session-list-create",
    ),
    path(
        "sessions/<int:pk>/",
        views.SessionRetrieveUpdateDestroyAPIView.as_view(),
        name="session-retrieve-update-destroy",
    ),
    # Speakers
    path(
        "<int:event_id>/speakers/",
        views.list_event_speakers,
        name="event-speakers-list",
    ),
    path(
        "<int:event_id>/speakers/add/",
        views.add_speaker_to_event,
        name="add-speaker-to-event",
    ),
    path(
        "<int:event_id>/speakers/remove/",
        views.remove_speaker_from_event,
        name="remove-speaker-from-event",
    ),
    # Sessions
    path(
        "<int:event_id>/sessions/",
        views.list_event_sessions,
        name="event-sessions-list",
    ),
    path(
        "<int:event_id>/sessions/create/",
        views.create_session_with_speaker,
        name="create-session-with-speaker",
    ),
    # Event detail with guest speakers (extended serializer)
    path(
        "detail/<int:pk>/",
        views.EventDetailAPIView.as_view(),
        name="event-detail-extended",
    ),
]
