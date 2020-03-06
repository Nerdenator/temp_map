from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TemperatureViewSet

router = DefaultRouter()

router.register('api', TemperatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard', include('temp_dashboard.urls'))
]