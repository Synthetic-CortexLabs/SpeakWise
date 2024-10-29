"""url routes for events."""

from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.EventCreateView.as_view(), name="event_create"),
    path("<int:pk>/", views.EventListView.as_view(), name="event_list"),
]
