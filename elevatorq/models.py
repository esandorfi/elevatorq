"""
ORM use 3 tables :
- Elevator
- PressBtnQ
- ElevatorQ
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

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
EQ_DEFAULT_ALGO = "elevatorq.look"


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


# ELEVATOR DEFINITION
# ------------------------------------------


class BuildingElevator(models.Model):
    """
    name: str
    id: int
    range_max_floor: int
    range_min_floor: int
    set_lobby_floor: int = 0
    status: ElevatorStatus = ElevatorStatus.DISABLED
    speed_floor: float = 2.1
    speed_openclose: float = 8.9
    algo: str = "look"
    """

    class Meta:
        verbose_name = verbose_name_plural = _("Building Elevators")
        ordering = [
            "name",
        ]

    # _v0
    name = models.CharField(max_length=10, help_text=_("Elevator unique name"))
    algo = models.CharField(
        max_length=100,
        default=EQ_DEFAULT_ALGO,
        help_text=_("extra - support different algorithm by building elevator"),
    )
    range_min_floor = models.SmallIntegerField(
        default=EQ_DEFAULT_MIN_FLOOR, help_text=_("elevator minimal start")
    )
    range_max_floor = models.SmallIntegerField(
        default=EQ_DEFAULT_MAX_FLOOR, help_text=_("elevator maximal stop")
    )
    lobby_floor = models.SmallIntegerField(
        default=EQ_DEFAULT_LOBBY_FLOOR,
        help_text=_(
            "extra - elevator lobby floor - allow elevator go to lobby or not if min floor > 0"
        ),
    )
    speed_floor = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=EQ_DEFAULT_SPEED_FLOOR,
        help_text=_("in simili seconds, elevator travel one floor"),
    )
    speed_open = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=EQ_DEFAULT_SPEED_OPEN,
        help_text=_("in simili seconds, opening door + people goes out/in"),
    )
    speed_close = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=EQ_DEFAULT_SPEED_CLOSE,
        help_text=_("in simili seconds, closing door"),
    )
    status = models.SmallIntegerField(
        choices=ElevatorStatus.choices,
        default=ElevatorStatus.DISABLED,
    )

    # _v1 : add main position status
    current_direction = models.CharField(
        max_length=4,
        choices=PositionDirection.choices,
        default=PositionDirection.IDLE,
    )
    current_floor = models.SmallIntegerField(default=0)

    def __str__(self):
        return _("Elevator {}").format(self.name)


# PRESS BUTTON PEOPLE Q
# ------------------------------------------


class PressBtnQ(models.Model):
    """
    direction: PositionDirection = PositionDirection.IDLE
    doors: PositionDoors = PositionDoors.CLOSE
    floor: int = 0
    """

    class Meta:
        verbose_name = verbose_name_plural = _("Press Button Q")
        ordering = [
            "create_time",
        ]

    # _v0
    direction = models.CharField(
        max_length=4,
        choices=PressBtnDirection.choices,
        default=PressBtnDirection.UP,
    )
    helptext = _("floor between min {} and max {} depends on your direction").format(
        EQ_DEFAULT_MIN_FLOOR, EQ_DEFAULT_MAX_FLOOR
    )
    start_floor = models.SmallIntegerField(
        help_text=helptext,
        validators=[
            MinValueValidator(EQ_DEFAULT_MIN_FLOOR),
            MaxValueValidator(EQ_DEFAULT_MAX_FLOOR),
        ],
    )
    final_floor = models.SmallIntegerField(
        help_text=helptext,
        validators=[
            MinValueValidator(EQ_DEFAULT_MIN_FLOOR),
            MaxValueValidator(EQ_DEFAULT_MAX_FLOOR),
        ],
    )
    create_time = models.TimeField(auto_now=True)

    elevator = models.ForeignKey(
        BuildingElevator,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    waiting_indicator = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    @property
    def pressbtn(self):
        """standardized press button display"""
        return f"{self.start_floor} {self.direction} {self.final_floor}"

    def __str__(self):
        if self.elevator:
            return _("{} -> Elevator {}").format(self.pressbtn, self.name)
        else:
            return self.pressbtn

    def clean(self):
        """validate data"""
        if (
            self.start_floor and self.final_floor
        ):  # wait standard validation before doing ours
            if self.direction == PressBtnDirection.DOWN:
                if self.start_floor <= self.final_floor:
                    raise ValidationError(
                        _("Start floor must be greater than final floor to go down.")
                    )

            elif self.direction == PressBtnDirection.UP:  # just to be clear
                if self.start_floor >= self.final_floor:
                    raise ValidationError(
                        _("Start floor must be lower than final floor to go up.")
                    )


# ELEVATOR FLUX Q
# ------------------------------------------


class ElevatorQ(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = _("Elevator Q")
        ordering = [
            "create_time",
        ]
        indexes = [
            models.Index(fields=["elevator", "create_time"]),
        ]

    # _v0
    create_time = models.TimeField(auto_now=True)
    elevator = models.ForeignKey(
        BuildingElevator,
        on_delete=models.CASCADE,
    )

    direction = models.CharField(
        max_length=4,
        choices=PositionDirection.choices,
        default=PositionDirection.IDLE,
    )
    floor = models.SmallIntegerField(
        validators=[
            MinValueValidator(EQ_DEFAULT_MIN_FLOOR),
            MaxValueValidator(EQ_DEFAULT_MAX_FLOOR),
        ],
    )
    door = models.SmallIntegerField(
        choices=DoorStatus.choices,
        default=DoorStatus.CLOSE,
    )
