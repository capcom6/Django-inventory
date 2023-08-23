from core import models
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = ["id", "name", "address", "created_date"]
