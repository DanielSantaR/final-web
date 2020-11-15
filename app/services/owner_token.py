from typing import List, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.owner_token import owner_token
from app.schemas.owner_token import CreateOwnerToken
from app.schemas.search import OwnerTokenQueryParams

QueryType = TypeVar("QueryType", bound=ICrudBase)


class OwnerTokenService:
    def __init__(self, owner_token_queries: QueryType):
        self.__owner_token_queries = owner_token_queries

    async def create_owner_token(
        self, owner_token: CreateOwnerToken
    ) -> Union[dict, None]:
        new_owner_token_id = await self.__owner_token_queries.create(obj_in=owner_token)
        return new_owner_token_id

    async def get_owner_token_by_id(self, owner_token_id: str) -> Union[dict, None]:
        owner_token = await self.__owner_token_queries.get_by_id(code=owner_token_id)
        if owner_token:
            return owner_token
        return None

    async def get_all(
        self, *, query_args: OwnerTokenQueryParams, skip: int, limit: int
    ) -> List:
        owner_token_data = query_args.__dict__
        payload = {
            key: value
            for (key, value) in owner_token_data.items()
            if value not in [None, ""]
        }
        owner_tokens = await self.__owner_token_queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return owner_tokens

    async def remove_owner_token(self, owner_token_id: str) -> int:
        owner_token_removed_id = await self.__owner_token_queries.delete(
            code=owner_token_id
        )
        return owner_token_removed_id


owner_token_service = OwnerTokenService(owner_token_queries=owner_token)
