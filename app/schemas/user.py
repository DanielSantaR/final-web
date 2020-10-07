from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    password: str
    color: Optional[str]


class CreateUserBase(BaseUser):
    department_: int
    rol_: int


class AuthUser(BaseModel):
    username: Optional[str]
    password: Optional[str]


class CreateUser(BaseUser):
    pass


class CompleteUser(BaseModel):
    department_: int
    rol_: int
    user_: Optional[int]
    is_busy: Optional[bool] = False
    is_active: Optional[bool] = True


class PayloadUser(BaseModel):
    username: Optional[str]
    password: Optional[str]
    color: Optional[str]


class UpdateUser(BaseModel):
    username: Optional[str]
    password: Optional[str]
    color: Optional[str]


class UpdateUserBase(UpdateUser):
    user: Optional[int]
    department: Optional[int]
    rol: Optional[int]
    is_busy: Optional[bool]
    is_active: Optional[bool]


class UpdateLastConnection(BaseModel):
    last_connection: Optional[str]


class UserInDB(BaseUser):
    id: int
    last_connection: Optional[str]
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: Optional[int]
    username: Optional[str]
    color: Optional[str]
    last_connection: Optional[str]
    created_at: Optional[datetime]
    last_modified: Optional[datetime]

    class Config:
        orm_mode = True


class UserCreated(BaseModel):
    id: int
    username: str
    color: Optional[str]
    last_connection: Optional[str]
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True
