from typing import Optional

from app.schemas.user import BaseUser, PayloadUser, UpdateUser, UserInDB


class BaseEmployee(BaseUser):
    username: str
    password: str


class CreateEmployee(BaseEmployee):
    pass


class PayloadEmployee(PayloadUser):
    username: Optional[str]


class UpdateEmployee(UpdateUser):
    username: Optional[str]
    password: Optional[str]


class EmployeeInDB(UserInDB):
    class Config:
        orm_mode = True
