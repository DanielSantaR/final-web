from tortoise import fields, models
from tortoise.fields.base import SET_NULL

from app.infra.postgres.models.vehicle_x_owner import VehicleXOwner


class Vehicle(models.Model):
    plate = fields.CharField(max_length=255, pk=True)
    brand = fields.CharField(max_length=255)
    model = fields.CharField(max_length=255)
    color = fields.CharField(max_length=255)
    vehicle_type = fields.CharField(max_length=255)
    state = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)
    creation_employee = fields.ForeignKeyField(
        "models.Employee",
        related_name="vehicles_created",
        on_delete=SET_NULL,
        null=True,
    )
    update_employee = fields.ForeignKeyField(
        "models.Employee",
        related_name="vehicles_updated",
        on_delete=SET_NULL,
        null=True,
    )

    vehicle_owners: fields.ReverseRelation[VehicleXOwner]
