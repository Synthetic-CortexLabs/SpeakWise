"""users urls."""

from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("users/register/", views.UserListView.as_view(), name="list"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="detail"),
    path("users/login/", views.UserLoginView.as_view(), name="login"),
    path("users/logout/", views.LogoutView.as_view(), name="logout"),
]
