from core import models
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import (
    PlaceSerializer,
    GroupSerializer,
    NomenclatureTypeSerializer,
    NomenclatureSerializer,
    NomenclatureInstanceSerializer,
    CharacteristicSerializer,
    # CharacteristicValueSerializer,
)


# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = models.Place.objects.all()
    serializer_class = PlaceSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = GroupSerializer


class NomenclatureTypeViewSet(viewsets.ModelViewSet):
    queryset = models.NomenclatureType.objects.all()
    serializer_class = NomenclatureTypeSerializer


class NomenclatureViewSet(viewsets.ModelViewSet):
    queryset = models.Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer


class NomenclatureInstanceViewSet(viewsets.ModelViewSet):
    queryset = models.NomenclatureInstance.objects.all()
    serializer_class = NomenclatureInstanceSerializer


class CharacteristicViewSet(viewsets.ModelViewSet):
    queryset = models.Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


# class CharacteristicValueViewSet(viewsets.ModelViewSet):
#     queryset = models.CharacteristicValue.objects.all()
#     serializer_class = CharacteristicValueSerializer
