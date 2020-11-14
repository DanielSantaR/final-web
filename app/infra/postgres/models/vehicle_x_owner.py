from tortoise import fields, models
from tortoise.fields.base import SET_NULL


class VehicleXOwner(models.Model):
    vehicle = fields.ForeignKeyField(
        "models.Vehicle",
        related_name="vehicle_owners",
        on_delete=SET_NULL,
        null=True,
    )
    owner = fields.ForeignKeyField(
        "models.Owner",
        related_name="owner_vehicles",
        on_delete=SET_NULL,
        null=True,
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        unique_together = ("vehicle", "owner")
