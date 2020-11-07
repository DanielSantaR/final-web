from typing import Any, Dict, List, Optional, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.reparation_detail import reparation_detail
from app.schemas.reparation_detail import CreateReparationDetail, UpdateReparationDetail
from app.schemas.search import ReparationDetailQueryParams

QueryType = TypeVar("QueryType", bound=ICrudBase)


class ReparationDetailService:
    def __init__(self, reparation_detail_queries: QueryType):
        self.__reparation_detail_queries = reparation_detail_queries

    async def create_reparation_detail(
        self, reparation_detail: CreateReparationDetail
    ) -> Union[dict, None]:
        new_reparation_detail_id = await self.__reparation_detail_queries.create(
            obj_in=reparation_detail
        )
        return new_reparation_detail_id

    async def get_reparation_detail_by_id(
        self, reparation_detail_id: int
    ) -> Union[dict, None]:
        reparation_detail = await self.__reparation_detail_queries.get_by_id(
            id=reparation_detail_id
        )
        if reparation_detail:
            return reparation_detail
        return None

    async def get_all(
        self, *, query_args: ReparationDetailQueryParams, skip: int, limit: int
    ) -> List:
        reparation_detail_data = query_args.__dict__
        payload = {
            key: value
            for (key, value) in reparation_detail_data.items()
            if value not in [None, ""]
        }
        reparation_details = await self.__reparation_detail_queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return reparation_details

    async def update_reparation_detail(
        self, reparation_detail_id: int, new_reparation_detail: UpdateReparationDetail
    ) -> Optional[Dict[str, Any]]:
        new_reparation_detail_data = new_reparation_detail.dict()
        payload = {
            key: value
            for (key, value) in new_reparation_detail_data.items()
            if value not in [None, ""]
        }
        current_update = await self.__reparation_detail_queries.update(
            id=reparation_detail_id, obj_in=payload
        )
        return current_update

    async def remove_reparation_detail(self, reparation_detail_id: int) -> int:
        reparation_detail_removed_id = await self.__reparation_detail_queries.delete(
            id=reparation_detail_id
        )
        return reparation_detail_removed_id


reparation_detail_service = ReparationDetailService(
    reparation_detail_queries=reparation_detail
)
