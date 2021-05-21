"""
Routes for API
"""


from rest_framework import routers
from .viewsets import ElevatorQViewSet, PressBtnQViewSet, BuildingElevatorViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"elevatorq", ElevatorQViewSet)
router.register(r"pressbtnq", PressBtnQViewSet)
router.register(r"building", BuildingElevatorViewSet)
