from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseVehicleXOwner(BaseModel):
    vehicle: str
    owner: str


class CreateVehicleXOwner(BaseVehicleXOwner):
    pass


class PayloadVehicleXOwner(BaseModel):
    vehicle: Optional[int]
    owner: Optional[str]


class UpdateVehicleXOwner(PayloadVehicleXOwner):
    pass


class VehicleXOwnerInDB(BaseVehicleXOwner):
    id: int
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True
