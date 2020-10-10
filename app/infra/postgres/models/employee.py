from tortoise import fields

from app.infra.postgres.models.user import User


class Employee(User):
    username = fields.CharField(unique=True, max_length=255)
    password = fields.TextField()
