from core import models
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PlaceSerializer


# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = models.Place.objects.all()
    serializer_class = PlaceSerializer
