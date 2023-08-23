from datetime import tzinfo
import zoneinfo

import pytz
from core import models

from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(
        # format="iso-8601", default_timezone=pytz.UTC
    )

    class Meta:
        model = models.Place
        fields = ["id", "name", "address", "created_date"]
