from django.urls import path, include
from rest_framework.routers import DefaultRouter
from temp_dashboard import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('temperatures', views.TemperatureViewSet)

urlpatterns = [
    path('', include(router.urls))
]