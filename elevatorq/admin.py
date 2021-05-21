"""
Enable default django-admin for our tables
"""

from django.contrib import admin
from .models import BuildingElevator, ElevatorQ, PressBtnQ


@admin.register(BuildingElevator)
class BuildingElevatorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "lobby_floor",
        "range_min_floor",
        "range_max_floor",
        "algo",
        "status",
        "current_direction",
        "current_floor",
    )
    readonly_fields = (
        "status",
        "current_direction",
        "current_floor",
    )


@admin.register(ElevatorQ)
class ElevatorQAdmin(admin.ModelAdmin):
    list_display = ("elevator", "direction", "floor", "door", "create_time")
    list_filter = ("elevator",)


@admin.register(PressBtnQ)
class PressBtnQAdmin(admin.ModelAdmin):
    list_display = ("pressbtn", "elevator", "waiting_indicator", "create_time")
    readonly_fields = (
        "elevator",
        "waiting_indicator",
    )
