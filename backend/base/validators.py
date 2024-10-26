from django.utils import timezone
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


def validate_date_time_values(start_time, end_time):
    if start_time > end_time:
        raise serializers.ValidationError(_("Start date should be before end date"))
    if start_time < timezone.now():
        raise serializers.ValidationError(_("Start date should be in the future"))
    if end_time < timezone.now():
        raise serializers.ValidationError(_("End date should be in the future"))
