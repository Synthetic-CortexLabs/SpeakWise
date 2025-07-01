"""user urls."""

from django.urls import path

from speakwise.users import views

app_name = "users"


urlpatterns = [
    path("users/register/", views.UserListView.as_view(), name="list_view"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="detail_view"),
    path("users/login/", views.UserLoginView.as_view(), name="login_view"),
    path("users/logout/", views.LogoutView.as_view(), name="logout_view"),
]
