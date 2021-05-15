"""
Simple Model for Elevators
"""

from enum import Enum


class ElevatorDirection(Enum):
    IDLE = 0
    TOP = 1
    DOWN = 2


class ElevatorStatus(Enum):
    DISABLED = 0
    ENABLED = 1
    ALERT = 99


class Elevator:
    floor = 0
    direction = ElevatorDirection.IDLE

    def __init__(self, name, status=ElevatorStatus.DISABLED):
        self.name = name
        self.status = status
