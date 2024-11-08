from django.urls import path

from speakwise.users.auth_views import RegisterView

app_name = "auth"

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="sign-up"),
]
