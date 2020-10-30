from datetime import datetime
from enum import Enum
from typing import Optional

from app.schemas.user import BaseUser, PayloadUser, UpdateUser, UserInDB


class Role(str, Enum):
    manager = "manager"
    assistant = "assistant"
    supervisor = "supervisor"
    technician = "technician"


class BaseEmployee(BaseUser):
    username: str
    is_active: bool = True
    role: Role


class CreateEmployee(BaseEmployee):
    password: str


class PayloadEmployee(PayloadUser):
    username: Optional[str]
    is_active: Optional[bool]
    role: Optional[str]


class UpdateEmployee(UpdateUser):
    username: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]
    role: Optional[Role]


class EmployeeInDB(UserInDB, BaseEmployee):
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True


class AuthEmployee(EmployeeInDB):
    password: str
