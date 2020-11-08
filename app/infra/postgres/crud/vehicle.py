from typing import Any, Dict, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.vehicle import Vehicle
from app.schemas.vehicle import CreateVehicle, UpdateVehicle

DB_KEYS = {
    "creation_employee": "creation_employee_id",
    "update_employee": "update_employee_id",
}


class CRUDVehicle(CRUDBase[Vehicle, CreateVehicle, UpdateVehicle]):
    async def get_by_id(self, *, plate: str) -> Union[dict, None]:
        model = await self.model.filter(plate=plate).first().values()
        if model:
            return model[0]
        return None

    async def update(self, *, plate: str, obj_in: Dict[str, Any]) -> Union[dict, None]:
        if not obj_in:
            model = await self.model.filter(plate=plate).first().values()
        else:
            model = await self.model.filter(plate=plate).update(**obj_in)
        if model:
            update_model = await self.model.filter(plate=plate).first().values()
            model_m = self.model(**update_model[0])
            update_fields = list(update_model[0].keys())
            await model_m.save(update_fields=update_fields)
            return update_model[0]
        return None

    async def delete(self, *, plate: str) -> int:
        model = await self.model.filter(plate=plate).first().delete()
        return model

    async def create(self, *, obj_in: CreateVehicle) -> Union[dict, None]:
        vehicle_data = obj_in.dict()
        vehicle = await self.model.create(**vehicle_data)
        return vehicle


vehicle = CRUDVehicle(Vehicle)
