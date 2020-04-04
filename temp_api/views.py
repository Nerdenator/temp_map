from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from temp_dashboard.models import Temperature, Sensor
from temp_api.serializers import TemperatureSerializer, SensorSerializer


@api_view(['GET', 'POST'])
def temperature_list(request):
    """
    Retrieve a temperature
    :param request: HTTP request
    :return: either a list of temperatures, or create a new one.
    """
    if request.method == 'GET':
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def temperature_latest(request, sensor_id, format=None):
    if request.method == 'GET':
        temperature = Temperature.objects.filter(sensor_id=sensor_id).latest()
        serializer = TemperatureSerializer(temperature, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def sensor_list(request, format=None):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)