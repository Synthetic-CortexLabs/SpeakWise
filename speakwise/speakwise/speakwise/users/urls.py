"""user urls."""

from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.UserList.as_view(), name="list_view"),
    path("<int:pk>/", views.UserDetailView.as_view(), name="detail_view"),
    path("login/", views.AuthenticateUser.as_view(), name="login_view"),
    path("logout/", views.UserLogoutView.as_view(), name="logout_view"),
]
