"""url routes for events."""

from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.EventCreateView.as_view()),
    path("<int:pk>/", views.EventListView.as_view()),
]
