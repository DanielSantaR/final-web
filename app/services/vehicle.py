from typing import Any, Dict, List, Optional, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.vehicle import vehicle
from app.schemas.search import VehicleQueryParams
from app.schemas.vehicle import CreateVehicle, UpdateVehicle

QueryType = TypeVar("QueryType", bound=ICrudBase)


class VehicleService:
    def __init__(self, vehicle_queries: QueryType):
        self.__vehicle_queries = vehicle_queries

    async def create_vehicle(self, vehicle: CreateVehicle) -> Union[dict, None]:
        new_vehicle_id = await self.__vehicle_queries.create(obj_in=vehicle)
        return new_vehicle_id

    async def get_vehicle_by_id(self, vehicle_id: str) -> Union[dict, None]:
        vehicle = await self.__vehicle_queries.get_by_id(plate=vehicle_id)
        if vehicle:
            return vehicle
        return None

    async def get_all(
        self, *, query_args: VehicleQueryParams, skip: int, limit: int
    ) -> List:
        vehicle_data = query_args.__dict__
        payload = {
            key: value
            for (key, value) in vehicle_data.items()
            if value not in [None, ""]
        }
        vehicles = await self.__vehicle_queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return vehicles

    async def update_vehicle(
        self, vehicle_id: str, new_vehicle: UpdateVehicle
    ) -> Optional[Dict[str, Any]]:
        new_vehicle_data = new_vehicle.dict()
        payload = {
            key: value
            for (key, value) in new_vehicle_data.items()
            if value not in [None, ""]
        }
        current_update = await self.__vehicle_queries.update(
            plate=vehicle_id, obj_in=payload
        )
        return current_update

    async def remove_vehicle(self, vehicle_id: str) -> int:
        vehicle_removed_id = await self.__vehicle_queries.delete(plate=vehicle_id)
        return vehicle_removed_id


vehicle_service = VehicleService(vehicle_queries=vehicle)
