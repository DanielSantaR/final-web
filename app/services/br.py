""" from typing import Any, Dict, List, Optional, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.br import br
from app.schemas.br import CreateBR, PayloadBR, UpdateBR

QueryType = TypeVar("QueryType", bound=ICrudBase)


class BRService:
    def __init__(self, br_queries: QueryType):
        self.__br_queries = br_queries

    async def create_br(self, br: CreateBR) -> Union[dict, None]:
        new_br_id = await self.__br_queries.create(obj_in=br)
        return new_br_id

    async def get_br_by_id(self, br_id: int) -> Union[dict, None]:
        br = await self.__br_queries.get_by_id(id=br_id)
        if br:
            return br
        return None

    async def get_all(self, *, br: PayloadBR, skip: int, limit: int) -> List:
        br_data = br.dict()
        payload = {
            key: value for (key, value) in br_data.items() if value not in [None, ""]
        }
        brs = await self.__br_queries.get_all(payload=payload, skip=skip, limit=limit)
        return brs

    async def update_br(self, br_id: int, new_br: UpdateBR) -> Optional[Dict[str, Any]]:
        new_br_data = new_br.dict()
        payload = {
            key: value
            for (key, value) in new_br_data.items()
            if value not in [None, ""]
        }
        current_update = await self.__br_queries.update(id=br_id, obj_in=payload)
        return current_update

    async def remove_br(self, br_id: int) -> int:
        br_removed_id = await self.__br_queries.delete(id=br_id)
        return br_removed_id


br_service = BRService(br_queries=br)
 """
