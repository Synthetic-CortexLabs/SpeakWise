"""organizers urls file."""

from django.urls import path
from . import views

app_name = "organizers"

urlpatterns = [
    path("organizers/", views.OrganizerListCreateView.as_view(), name="list_view"),
    path(
        "organizers/<int:pk>/", views.OrganizerDetailView.as_view(), name="detail_view"
    ),
]
