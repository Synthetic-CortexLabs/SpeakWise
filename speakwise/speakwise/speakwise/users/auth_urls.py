from django.urls import path
from .auth_views import RegisterView

urlpatterns = [
   path("signup/",RegisterView.as_view(),name="sign-up"),
]