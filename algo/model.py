"""
Simple Model for Elevators
"""
from dataclasses import dataclass
from enum import Enum
from typing import List
import re


class PositionDirection(Enum):
    IDLE = "IDLE"
    UP = "UP"
    DOWN = "DOWN"


class PositionDoors(Enum):
    OPEN = 1
    CLOSE = 0


class ElevatorStatus(Enum):
    """ General Elevator status """

    DISABLED = 0
    ENABLED = 1
    ALERT = 99


@dataclass
class ElevatorDefinition:
    """ Describe the Elevator properties """

    name: str
    id: int
    range_max_floor: int
    range_min_floor: int
    set_lobby_floor: int = 0
    status: ElevatorStatus = ElevatorStatus.DISABLED
    speed_floor: float = 2.1
    speed_openclose: float = 8.9
    algo: str = "look"


@dataclass
class ElevatorPosition:
    """ Temporary elevator position """

    direction: PositionDirection = PositionDirection.IDLE
    doors: PositionDoors = PositionDoors.CLOSE
    floor: int = 0


# regex_input_mask = re.compile("(\\d+)([a-zA-Z]+)(\\d+)")


input_people_q = [
    "0UP10",
    "13UP20",
    "2UP5",
    "0UP47",
    "10UP30",
    "20DOWN0",
    "20DOWN10",
    "22DOWN20",
    "20UP45",
]


def validate_input_people(q: List[str]):
    """ sample q : ["0UP10", "13UP20", "2UP5", "0UP47", "10UP30", "20DOWN0", "20DOWN10"]
    """
    regex_mask = re.compile("(\d+)(UP|DOWN)(\d+)")
    for i in q:
        # because of regex mask we sure to get correct typed data, instead raise
        try:
            m = regex_mask.match(i)
            start_floor = m.group(1)
            direction = m.group(2)
            final_floor = m.group(3)
        except Exception:
            raise ValueError(f"input_people_eq {i} regex mask format error")

        # because of regex mask, we sure of UP or DOWN
        if PositionDirection(direction) == PositionDirection.DOWN:
            if final_floor >= start_floor:
                raise ValueError(
                    f"input_people_eq {i} -> {direction} > {start_floor} can't be lower than {final_floor}"
                )
        else:
            if start_floor >= final_floor:
                raise ValueError(
                    f"input_people_eq {i} -> {direction} > {start_floor} can't be greater than {final_floor}"
                )

        print(f"Find {direction} -> {start_floor} to {final_floor}")


validate_input_people(input_people_q)
