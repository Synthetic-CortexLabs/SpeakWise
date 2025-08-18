"""user admin."""

from django.contrib import admin

from speakwise.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin view for the User model."""

    list_display = ("username", "email", "is_active", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_active", "is_staff")
    ordering = ("-date_joined",)
