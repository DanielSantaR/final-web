from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseVehicle(BaseModel):
    plate: str
    brand: str
    model: str
    color: str
    vehicle_type: str
    state: str


class CreateVehicle(BaseVehicle):
    creation_employee: str
    update_employee: str


class PayloadVehicle(BaseModel):
    plate: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    color: Optional[str]
    vehicle_type: Optional[str]
    state: Optional[str]


class UpdateVehicle(BaseModel):
    update_employee: str
    plate: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    color: Optional[str]
    vehicle_type: Optional[str]
    state: Optional[str]


class VehicleInDB(BaseVehicle):
    # id: int
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True