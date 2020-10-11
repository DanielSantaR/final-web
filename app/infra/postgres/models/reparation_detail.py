from tortoise import fields, models
from tortoise.fields.base import SET_NULL


class ReparationDetail(models.Model):
    vehicle = fields.ForeignKeyField(
        "models.Vehicle", related_name="vehicles", on_delete=SET_NULL, null=True,
    )
    employee = fields.ForeignKeyField(
        "models.Employee", related_name="employees", on_delete=SET_NULL, null=True,
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)
    description = fields.CharField(max_length=255)
    cost = fields.FloatField(default=0)
    spare_parts = fields.JSONField(null=True)
    state = fields.CharField(max_length=255)
