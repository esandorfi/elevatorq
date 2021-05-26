"""
Routes for API
"""

from django.urls import path
from rest_framework import routers
from .viewsets import (
    ElevatorQViewSet,
    PressBtnQViewSet,
    BuildingElevatorViewSet,
    DisplayElevatorQ,
    DisplayWaitinIndicatorLobbyQ,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"elevatorq", ElevatorQViewSet)
router.register(r"pressbtnq", PressBtnQViewSet)
router.register(r"building", BuildingElevatorViewSet)


urlpatterns = [
    path("displayq/", DisplayElevatorQ.as_view()),
    path("waitingindicator/floor/0/", DisplayWaitinIndicatorLobbyQ.as_view()),
] + router.urls
