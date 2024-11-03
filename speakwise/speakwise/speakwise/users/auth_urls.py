from django.urls import path
from .auth_views import SignUpView

urlpatterns = [
    path("signup/",SignUpView.as_view(),name="sign-up")
]