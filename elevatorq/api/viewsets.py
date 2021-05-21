"""
Public API 
"""

from rest_framework import viewsets
from ..models import ElevatorQ, PressBtnQ, BuildingElevator
from .serializers import (
    ElevatorQSerializer,
    PressBtnQSerializer,
    BuildingElevatorSerializer,
)


class ElevatorQViewSet(viewsets.ModelViewSet):
    queryset = ElevatorQ.objects.all()
    serializer_class = ElevatorQSerializer


class PressBtnQViewSet(viewsets.ModelViewSet):
    queryset = PressBtnQ.objects.all()
    serializer_class = PressBtnQSerializer


#
# might be optional
#


class BuildingElevatorViewSet(viewsets.ModelViewSet):
    queryset = BuildingElevator.objects.all()
    serializer_class = BuildingElevatorSerializer
