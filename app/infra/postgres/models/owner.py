from tortoise import fields
from tortoise.fields.base import SET_NULL

from app.infra.postgres.models.user import User


class Owner(User):
    creation_employee = fields.ForeignKeyField(
        "models.Employee", related_name="owners_created", on_delete=SET_NULL, null=True,
    )
    update_employee = fields.ForeignKeyField(
        "models.Employee", related_name="owners_updated", on_delete=SET_NULL, null=True,
    )
