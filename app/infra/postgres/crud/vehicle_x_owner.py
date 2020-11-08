from typing import Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.vehicle_x_owner import VehicleXOwner
from app.schemas.vehicle_x_owner import CreateVehicleXOwner, UpdateVehicleXOwner


class CRUDVehicleXOwner(
    CRUDBase[VehicleXOwner, CreateVehicleXOwner, UpdateVehicleXOwner]
):
    async def get_by_id(self, *, id: int) -> Union[dict, None]:
        model = await self.model.filter(id=id).first().values()
        if model:
            return model[0]
        return None

    async def delete(self, *, id: int) -> int:
        model = await self.model.filter(id=id).first().delete()
        return model

    async def create(self, *, obj_in: CreateVehicleXOwner) -> Union[dict, None]:
        vehicle_x_owner_data = obj_in.dict()
        vehicle_x_owner = await self.model.create(**vehicle_x_owner_data,)
        return vehicle_x_owner


vehicle_x_owner = CRUDVehicleXOwner(VehicleXOwner)
