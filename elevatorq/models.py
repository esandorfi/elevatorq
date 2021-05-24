"""
Define the settings of ElevatorQ application for the ORM, ....
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

# load the application shared settings
from . import appsettings


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
        default=appsettings.EQ_DEFAULT_ALGO,
        help_text=_("extra - support different algorithm by building elevator"),
        choices=appsettings.EQ_ALGO,
    )
    range_min_floor = models.SmallIntegerField(
        default=appsettings.EQ_DEFAULT_MIN_FLOOR, help_text=_("elevator minimal start")
    )
    range_max_floor = models.SmallIntegerField(
        default=appsettings.EQ_DEFAULT_MAX_FLOOR, help_text=_("elevator maximal stop")
    )
    lobby_floor = models.SmallIntegerField(
        default=appsettings.EQ_DEFAULT_LOBBY_FLOOR,
        help_text=_(
            "extra - elevator lobby floor - allow elevator go to lobby or not if min floor > 0"
        ),
    )
    speed_floor = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=appsettings.EQ_DEFAULT_SPEED_FLOOR,
        help_text=_("in simili seconds, elevator travel one floor"),
    )
    speed_open = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=appsettings.EQ_DEFAULT_SPEED_OPEN,
        help_text=_("in simili seconds, opening door + people goes out/in"),
    )
    speed_close = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=appsettings.EQ_DEFAULT_SPEED_CLOSE,
        help_text=_("in simili seconds, closing door"),
    )
    status = models.SmallIntegerField(
        choices=appsettings.ElevatorStatus.choices,
        default=appsettings.ElevatorStatus.DISABLED,
    )

    # _v1 : add main position status
    current_direction = models.CharField(
        max_length=4,
        choices=appsettings.PositionDirection.choices,
        default=appsettings.PositionDirection.IDLE,
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
        choices=appsettings.PressBtnDirection.choices,
        default=appsettings.PressBtnDirection.UP,
    )
    helptext = _("floor between min {} and max {} depends on your direction").format(
        appsettings.EQ_DEFAULT_MIN_FLOOR, appsettings.EQ_DEFAULT_MAX_FLOOR
    )
    start_floor = models.SmallIntegerField(
        help_text=helptext,
        validators=[
            MinValueValidator(appsettings.EQ_DEFAULT_MIN_FLOOR),
            MaxValueValidator(appsettings.EQ_DEFAULT_MAX_FLOOR),
        ],
    )
    final_floor = models.SmallIntegerField(
        help_text=helptext,
        validators=[
            MinValueValidator(appsettings.EQ_DEFAULT_MIN_FLOOR),
            MaxValueValidator(appsettings.EQ_DEFAULT_MAX_FLOOR),
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
            if self.direction == appsettings.PressBtnDirection.DOWN:
                if self.start_floor <= self.final_floor:
                    raise ValidationError(
                        _("Start floor must be greater than final floor to go down.")
                    )

            elif self.direction == appsettings.PressBtnDirection.UP:  # just to be clear
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
        choices=appsettings.PositionDirection.choices,
        default=appsettings.PositionDirection.IDLE,
    )
    # warning with lobby definition
    # needs to be managed
    floor = models.SmallIntegerField(
        validators=[
            MinValueValidator(appsettings.EQ_DEFAULT_MIN_FLOOR),
            MaxValueValidator(appsettings.EQ_DEFAULT_MAX_FLOOR),
        ],
    )
    door = models.SmallIntegerField(
        choices=appsettings.DoorStatus.choices,
        default=appsettings.DoorStatus.CLOSE,
    )

    def __str__(self):
        # we are sure the variables have a default or are requiered
        return _("floor {} direction {} door {}").format(
            self.floor, self.direction, self.door
        )
