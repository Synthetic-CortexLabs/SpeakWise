"""Extended event serializers with more detailed speaker and session information."""

from rest_framework import serializers
from .serializers import EventSerializer, SessionSerializer


# is this really necessary? I think we can add this to the serializers file and inherit from the EventSerializer as we did here.
