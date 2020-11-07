from datetime import datetime
from typing import Optional

from app.schemas.user import BaseUser, UpdateUser, UserInDB


class BaseOwner(BaseUser):
    pass


class CreateOwner(BaseOwner):
    creation_employee: str
    update_employee: str


class UpdateOwner(UpdateUser):
    update_employee: Optional[str]
    vehicle: Optional[int]


class OwnerInDB(UserInDB):
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True
