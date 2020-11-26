from typing import List, Union

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

    async def get_all_owner_vehicles(
        self, *, owner_id: str, skip: int = 0, limit: int = 99999
    ) -> List:
        model = (
            await self.model.filter(owner_id=owner_id)
            .offset(skip)
            .limit(limit)
            .all()
            .values(
                plate="vehicle_id",
                brand="vehicle__brand",
                model="vehicle__model",
                color="vehicle__color",
                vehicle_type="vehicle__vehicle_type",
                state="vehicle__state",
                creation_employee_id="vehicle__creation_employee__identity_card",
                update_employee_id="vehicle__update_employee__identity_card",
                created_at="vehicle__created_at",
                last_modified="vehicle__last_modified",
            )
        )
        return model

    async def get_all_vehicle_owners(
        self, *, vehicle_id: str, skip: int = 0, limit: int = 99999
    ) -> List:
        model = (
            await self.model.filter(vehicle_id=vehicle_id)
            .offset(skip)
            .limit(limit)
            .all()
            .values(
                identity_card="owner_id",
                names="owner__names",
                surnames="owner__surnames",
                phone="owner__phone",
                email="owner__email",
                creation_employee_id="owner__creation_employee__identity_card",
                update_employee_id="owner__update_employee__identity_card",
                created_at="owner__created_at",
                last_modified="owner__last_modified",
            )
        )
        return model

    async def delete_owner_vehicle(self, *, owner_id: str, vehicle_id: str) -> int:
        model = (
            await self.model.filter(owner_id=owner_id, vehicle_id=vehicle_id)
            .first()
            .delete()
        )
        return model

    async def create(self, *, obj_in: CreateVehicleXOwner) -> Union[dict, None]:
        vehicle_x_owner_data = obj_in.dict()
        vehicle_x_owner = await self.model.create(
            **vehicle_x_owner_data,
        )
        return vehicle_x_owner


vehicle_x_owner = CRUDVehicleXOwner(VehicleXOwner)
