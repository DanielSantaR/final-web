from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


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
    owners: List[str] = Field(..., min_items=1)


class UpdateVehicle(BaseModel):
    update_employee: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    color: Optional[str]
    vehicle_type: Optional[str]
    state: Optional[str]
    owners: Optional[List[str]] = Field(None, min_items=1)


class VehicleInDB(BaseVehicle):
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True
