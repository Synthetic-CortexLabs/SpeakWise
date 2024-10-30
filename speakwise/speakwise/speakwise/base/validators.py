"""Validators for the base app."""

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


def validate_date_time_values(start_date, end_date):
    """Validate the start and end date values."""
    if start_date > end_date:
        raise serializers.ValidationError(
            _("The end date must be after the start date.")
        )
    if start_date < timezone.now():
        raise serializers.ValidationError(_("The start date must be in the future."))
    if end_date < timezone.now():
        raise serializers.ValidationError(_("The end date must be in the future."))
