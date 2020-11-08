from tortoise import fields

from app.infra.postgres.models.owner import Owner
from app.infra.postgres.models.user import User
from app.infra.postgres.models.vehicle import Vehicle


class Employee(User):
    username = fields.CharField(unique=True, max_length=255)
    password = fields.CharField(max_length=255)
    role = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)

    owners_created: fields.ReverseRelation[Owner]
    owners_updated: fields.ReverseRelation[Owner]

    vehicles_created: fields.ReverseRelation[Vehicle]
    vehicles_updated: fields.ReverseRelation[Vehicle]
