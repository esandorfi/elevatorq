"""
Public API for ElevatorQ and PressBtnQ
"""

from rest_framework import serializers
from ..models import ElevatorQ, PressBtnQ, BuildingElevator


class ElevatorQSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElevatorQ
        fields = "__all__"


class PressBtnQSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PressBtnQ
        fields = "__all__"


#
# might be optional
#


class BuildingElevatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuildingElevator
        fields = "__all__"
