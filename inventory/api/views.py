from django.http import HttpRequest
from core import models
from django.shortcuts import render
from rest_framework import viewsets, exceptions, serializers

from .serializers import GroupSerializer, PlaceSerializer


# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = models.Place.objects.all()
    serializer_class = PlaceSerializer


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer

    def validate_place_id(self) -> int:
        place_id = self.request.parser_context.get("kwargs").get("place_id")
        if not models.Place.objects.filter(pk=place_id).exists():
            raise exceptions.NotFound()
        return place_id

    def get_queryset(self):
        place_id = self.validate_place_id()

        queryset = models.Group.objects.filter(place_id=place_id)

        if "nomenclature__name" in self.request.query_params:
            queryset = queryset.filter(
                nomenclatureinstance__nomenclature__name__contains=self.request.query_params[
                    "nomenclature__name"
                ]
            )

        return queryset.all()

    def perform_create(self, serializer: serializers.Serializer):
        place_id = self.validate_place_id()

        serializer.save(place_id=place_id)
