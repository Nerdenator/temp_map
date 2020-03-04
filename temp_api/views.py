from rest_framework import viewsets

from temp_dashboard.models import Temperature
from temp_api.serializers import TemperatureSerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def perform_create(self, serializer):
        serializer.save()
