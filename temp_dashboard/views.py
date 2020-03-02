from django.shortcuts import render
from rest_framework import viewsets

from .models import Temperature, Sensor
from .serializers import TemperatureSerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def perform_create(self, serializer):
        serializer.save()