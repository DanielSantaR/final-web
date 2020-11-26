from typing import Any, Dict, List, Optional, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.vehicle_x_owner import vehicle_x_owner
from app.schemas.search import VehicleXOwnerQueryParams
from app.schemas.vehicle_x_owner import CreateVehicleXOwner, UpdateVehicleXOwner

QueryType = TypeVar("QueryType", bound=ICrudBase)


class VehicleXOwnerService:
    def __init__(self, vehicle_x_owner_queries: QueryType):
        self.__vehicle_x_owner_queries = vehicle_x_owner_queries

    async def create_vehicle_x_owner(
        self, vehicle_x_owner: CreateVehicleXOwner
    ) -> Union[dict, None]:
        new_vehicle_x_owner_id = await self.__vehicle_x_owner_queries.create(
            obj_in=vehicle_x_owner
        )
        return new_vehicle_x_owner_id

    async def get_vehicle_x_owner_by_id(
        self, vehicle_x_owner_id: str
    ) -> Union[dict, None]:
        vehicle_x_owner = await self.__vehicle_x_owner_queries.get_by_id(
            id=vehicle_x_owner_id
        )
        if vehicle_x_owner:
            return vehicle_x_owner
        return None

    async def get_all(
        self, *, query_args: VehicleXOwnerQueryParams, skip: int, limit: int
    ) -> List:
        vehicle_x_owner_data = query_args.__dict__
        payload = {
            key: value
            for (key, value) in vehicle_x_owner_data.items()
            if value not in [None, ""]
        }
        vehicle_x_owners = await self.__vehicle_x_owner_queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return vehicle_x_owners

    async def get_all_owner_vehicles(
        self, *, owner_id: str, skip: int, limit: int
    ) -> List:
        vehicle_x_owners = await self.__vehicle_x_owner_queries.get_all_owner_vehicles(
            owner_id=owner_id, skip=skip, limit=limit
        )
        return vehicle_x_owners

    async def get_all_vehicle_owners(
        self, *, vehicle_id: str, skip: int, limit: int
    ) -> List:
        vehicle_x_owners = await self.__vehicle_x_owner_queries.get_all_vehicle_owners(
            vehicle_id=vehicle_id, skip=skip, limit=limit
        )
        return vehicle_x_owners

    async def update_vehicle_x_owner(
        self, vehicle_x_owner_id: str, new_vehicle_x_owner: UpdateVehicleXOwner
    ) -> Optional[Dict[str, Any]]:
        new_vehicle_x_owner_data = new_vehicle_x_owner.dict()
        payload = {
            key: value
            for (key, value) in new_vehicle_x_owner_data.items()
            if value not in [None, ""]
        }
        current_update = await self.__vehicle_x_owner_queries.update(
            id=vehicle_x_owner_id, obj_in=payload
        )
        return current_update

    async def remove_vehicle_x_owner(self, vehicle_x_owner_id: int) -> int:
        vehicle_x_owner_removed_id = await self.__vehicle_x_owner_queries.delete(
            id=vehicle_x_owner_id
        )
        return vehicle_x_owner_removed_id

    async def remove_vehicle_x_owner_by_id(self, owner_id: str, vehicle_id: str) -> int:
        vehicle_x_owner_removed_id = (
            await self.__vehicle_x_owner_queries.delete_owner_vehicle(
                owner_id=owner_id, vehicle_id=vehicle_id
            )
        )
        return vehicle_x_owner_removed_id


vehicle_x_owner_service = VehicleXOwnerService(vehicle_x_owner_queries=vehicle_x_owner)
