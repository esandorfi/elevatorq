"""
ORM use 3 tables :
- Elevator
- PressBtnQ
- ElevatorQ
"""

from django.db import models

# SETTINGS ORM VERSION
# ------------------------------------------
"""
Please increment number and notify 
when any orm or setting changes are applied
"""
SETTINGS_ORM_VERSION = 1


# SOME DEFAULTS HARD CODED
# ------------------------------------------

# building floors
EQ_DEFAULT_MIN_FLOOR = 0  # elevator minimal start
EQ_DEFAULT_MAX_FLOOR = 47  # elevator maximal stop

# default elevator speeds
EQ_DEFAULT_SPEED_FLOOR = 2.1  # in simili seconds, elevator travel one floor
EQ_DEFAULT_SPEED_OPEN = 8.4  # in simili seconds, opening door + people goes out/in
EQ_DEFAULT_SPEED_CLOSE = 3.7  # in simili seconds, closing door

# extra - elevator lobby floor - allow elevator go to lobby or not if min floor > 0
EQ_DEFAULT_LOBBY_FLOOR = 0

# extra - support different algorithm by building elevator
EQ_DEFAULT_ALGO = "elevatorq.algo.look"


# ENUM VALUES
# ------------------------------------------


class DoorStatus(models.IntegerChoices):
    # _v0
    OPEN = 1
    CLOSE = 0


class PressBtnDirection(models.TextChoices):
    # _v0
    UP = "UP"
    DOWN = "DOWN"


class PositionDirection(models.TextChoices):
    # _v0
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"


class ElevatorStatus(models.IntegerChoices):
    # _v0
    DISABLED = 0
    ENABLED = 1
    ALERT = 99
