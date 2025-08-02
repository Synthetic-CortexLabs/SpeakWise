"""organizers urls file."""

from django.urls import path

from . import views

app_name = "organizers"

urlpatterns = [
    path("organizers/", views.OrganizerListCreateView.as_view(), name="list_view"),
    path(
        "organizers/<int:pk>/",
        views.OrganizerDetailView.as_view(),
        name="detail_view",
    ),
    path(
        "organizers/attendance-list/",
        views.FileUploadViewCreatView.as_view(),
        name="attendance-list",
    ),
    path(
        "organizers/attendance-list/<int:pk>/",
        views.FileUploadDetailview.as_view(),
        name="attendance-detail",
    ),
]
