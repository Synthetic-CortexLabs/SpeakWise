from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    # Events
    path("events/", views.EventListCreateAPIView.as_view(), name="event-list-create"),
    path(
        "events/<int:pk>/",
        views.EventRetrieveUpdateDestroyAPIView.as_view(),
        name="event-retrieve-update-destroy",
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
]
