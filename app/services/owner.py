from typing import Any, Dict, List, Optional, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.owner import owner
from app.schemas.owner import CreateOwner, UpdateOwner
from app.schemas.search import OwnerQueryParams

QueryType = TypeVar("QueryType", bound=ICrudBase)


class OwnerService:
    def __init__(self, owner_queries: QueryType):
        self.__owner_queries = owner_queries

    async def create_owner(self, owner: CreateOwner) -> Union[dict, None]:
        new_owner_id = await self.__owner_queries.create(obj_in=owner)
        return new_owner_id

    async def get_owner_by_id(self, owner_id: str) -> Union[dict, None]:
        owner = await self.__owner_queries.get_by_id(identity_card=owner_id)
        if owner:
            return owner
        return None

    async def get_all(
        self, *, query_args: OwnerQueryParams, skip: int, limit: int
    ) -> List:
        owner_data = query_args.__dict__
        payload = {
            key: value for (key, value) in owner_data.items() if value not in [None, ""]
        }
        owners = await self.__owner_queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return owners

    async def update_owner(
        self, owner_id: str, new_owner: UpdateOwner
    ) -> Optional[Dict[str, Any]]:
        new_owner_data = new_owner.dict()
        payload = {
            key: value
            for (key, value) in new_owner_data.items()
            if value not in [None, ""]
        }
        current_update = await self.__owner_queries.update(
            identity_card=owner_id, obj_in=payload
        )
        return current_update

    async def remove_owner(self, owner_id: int) -> int:
        owner_removed_id = await self.__owner_queries.delete(identity_card=owner_id)
        return owner_removed_id


owner_service = OwnerService(owner_queries=owner)
