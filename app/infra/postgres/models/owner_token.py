from tortoise import fields, models


class OwnerToken(models.Model):
    code = fields.CharField(max_length=255)
    owner_id = fields.CharField(max_length=255)
    token = fields.CharField(max_length=255)
    token_type = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
