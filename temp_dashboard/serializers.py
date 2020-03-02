from rest_framework import serializers
from .models import Temperature, Sensor


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['id', 'sensor', 'time', 'fahrenheit', 'celsius']