from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    # Events
    path("", views.EventListCreateAPIView.as_view(), name="event-list-create"),
    path(
        "<int:pk>/",
        views.EventRetrieveUpdateDestroyAPIView.as_view(),
        name="event-retrieve-update-destroy",
    ),
    # Regions
    path(
        "regions/",
        views.RegionListCreateAPIView.as_view(),
        name="region-list-create",
    ),
    path(
        "regions/<int:pk>/",
        views.RegionRetrieveUpdateDestroyAPIView.as_view(),
        name="region-retrieve-update-destroy",
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
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
