from tortoise import fields, models


class User(models.Model):
    username = fields.CharField(unique=True, max_length=255)
    password = fields.TextField()
    last_connection = fields.TextField(null=True)
    color = fields.CharField(null=True, max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)
