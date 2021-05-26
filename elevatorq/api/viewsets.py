"""
Public API 
"""

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import ElevatorQ, PressBtnQ, BuildingElevator
from .serializers import (
    ElevatorQSerializer,
    PressBtnQSerializer,
    BuildingElevatorSerializer,
)

from elevatorq.algo.eq import DispatchSystem, ResetDatabase

#
# SIMPLE ELEVATORQ MONITORING
#


class DisplayElevatorQ(APIView):
    def get(self, request, format=None):
        display = DispatchSystem()
        displayq = display.display_elevator_q()
        return Response(displayq)


class DisplayWaitinIndicatorLobbyQ(APIView):
    def get(self, request, format=None):
        display = DispatchSystem()
        displayq = display.display_elevator_q(waiting_floor=0)
        return Response(displayq)


#
# STANDARD API ROUTE
#


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
