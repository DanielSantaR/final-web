from typing import Any, Dict, List, Optional, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.user import user
from app.schemas.user import CreateUser, PayloadUser, UpdateUser

QueryType = TypeVar("QueryType", bound=ICrudBase)


class UserService:
    def __init__(self, user_queries: QueryType):
        self.__user_queries = user_queries

    async def create_user(self, user: CreateUser) -> Union[dict, None]:
        new_user_id = await self.__user_queries.create(obj_in=user)
        return new_user_id

    async def get_user_by_id(self, user_id: int) -> Union[dict, None]:
        user = await self.__user_queries.get_by_id(id=user_id)
        if user:
            return user
        return None

    async def get_all(self, *, user: PayloadUser, skip: int, limit: int) -> List:
        user_data = user.dict()
        payload = {
            key: value for (key, value) in user_data.items() if value not in [None, ""]
        }
        users = await self.__user_queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return users

    async def update_user(
        self, user_id: int, new_user: UpdateUser
    ) -> Optional[Dict[str, Any]]:
        new_user_data = new_user.dict()
        payload = {
            key: value
            for (key, value) in new_user_data.items()
            if value not in [None, ""]
        }
        current_update = await self.__user_queries.update(id=user_id, obj_in=payload)
        return current_update

    async def remove_user(self, user_id: int) -> int:
        user_removed_id = await self.__user_queries.delete(id=user_id)
        return user_removed_id


user_service = UserService(user_queries=user)
