from typing import Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.vehicle_x_owner import VehicleXOwner
from app.schemas.vehicle_x_owner import CreateVehicleXOwner, UpdateVehicleXOwner
from app.utils.get_keys import get_right_keys

DB_KEYS = {
    "owner": "owner_id",
    "vehicle": "vehicle_id",
}


class CRUDVehicleXOwner(
    CRUDBase[VehicleXOwner, CreateVehicleXOwner, UpdateVehicleXOwner]
):
    async def get_by_id(self, *, vehicle: str, owner: str) -> Union[dict, None]:
        model = (
            await self.model.filter(vehicle_id=vehicle, owner_id=owner).first().values()
        )
        if model:
            return model[0]
        return None

    async def delete(self, *, vehicle: str, owner: str) -> int:
        model = (
            await self.model.filter(vehicle_id=vehicle, owner_id=owner).first().delete()
        )
        return model

    async def create(self, *, obj_in: CreateVehicleXOwner) -> Union[dict, None]:
        vehicle_x_owner_data = obj_in.dict()
        vehicle_x_owner_data = get_right_keys(
            payload=vehicle_x_owner_data, db_keys=DB_KEYS
        )
        vehicle_x_owner = await self.model.create(**vehicle_x_owner_data,)
        return vehicle_x_owner


vehicle_x_owner = CRUDVehicleXOwner(VehicleXOwner)
