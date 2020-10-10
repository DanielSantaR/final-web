from tortoise import fields, models


class User(models.Model):
    identity_card = fields.CharField(max_length=255, pk=True)
    names = fields.CharField(max_length=255)
    surnames = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True
