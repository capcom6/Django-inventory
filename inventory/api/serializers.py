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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ["place", "comment"]


class NomenclatureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NomenclatureType
        fields = []


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nomenclature
        fields = ["type", "characteristics"]


class NomenclatureInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NomenclatureInstance
        fields = ["nomenclature", "group", "quantity", "comment"]


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Characteristic
        fields = ["type"]


# class CharacteristicValueSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CharacteristicValue
#         fields = ["value", "characteristic", "nomeclature"]
