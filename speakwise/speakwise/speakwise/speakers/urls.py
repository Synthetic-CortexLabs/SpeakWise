"""Speakers URLs."""

from django.urls import path

from speakwise.speakers import views

urlpatterns = [
    path("", views.SpeakerProfileList.as_view(), name="speaker-list"),
    path("<int:pk>/", views.SpeakerProfileDetail.as_view(), name="speaker-detail"),
    path("<int:pk>/dashboard/", views.speaker_dashboard, name="speaker-dashboard"),
    path("skills/", views.SkillTagList.as_view(), name="skill-list"),
    path("skills/<int:pk>/", views.SkillTagDetail.as_view(), name="skill-detail"),
    path(
        "social-links/", views.SpeakerSocialLinkList.as_view(), name="social-link-list"
    ),
    path(
        "social-links/<int:pk>/",
        views.SpeakerSocialLinkDetail.as_view(),
        name="social-link-detail",
    ),
]
