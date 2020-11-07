from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class BaseReparationDetail(BaseModel):
    description: str
    cost: Optional[float]
    spare_parts: Optional[List[str]]
    state: str


class CreateReparationDetail(BaseReparationDetail):
    vehicle: str
    employee: str


class PayloadReparationDetail(BaseModel):
    vehicle: Optional[int]
    employee: Optional[str]
    state: Optional[str]


class UpdateReparationDetail(BaseModel):
    description: Optional[str]
    cost: Optional[float]
    spare_parts: Optional[List[str]]
    state: Optional[str]


class ReparationDetailInDB(BaseReparationDetail):
    id: int
    vehicle_id: str
    employee_id: str
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True
