from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseVehicle(BaseModel):
    plate: str
    brand: str
    model: str
    color: str
    vehicle_type: str
    state: str = "received"
    creation_employee_id: str
    update_employee_id: str


class CreateVehicle(BaseVehicle):
    pass


class UpdateVehicle(BaseModel):
    update_employee_id: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    color: Optional[str]
    vehicle_type: Optional[str]
    state: Optional[str]


class VehicleInDB(BaseVehicle):
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True
