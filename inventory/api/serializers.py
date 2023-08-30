from core import models
from rest_framework import serializers

COMMON_FIELDS = ["id", "status", "name"]


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = COMMON_FIELDS + ["address", "created_date", "updated_date"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = COMMON_FIELDS + ["comment", "created_date", "updated_date"]
