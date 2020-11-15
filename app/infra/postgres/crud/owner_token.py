from typing import Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.owner_token import OwnerToken
from app.schemas.owner_token import CreateOwnerToken, UpdateOwnerToken


class CRUDOwnerToken(CRUDBase[OwnerToken, CreateOwnerToken, UpdateOwnerToken]):
    async def get_by_id(self, *, code: str) -> Union[dict, None]:
        model = await self.model.filter(code=code).first().values()
        if model:
            return model[0]
        return None

    async def delete(self, *, code: str) -> int:
        model = await self.model.filter(code=code).first().delete()
        return model

    async def create(self, *, obj_in: CreateOwnerToken) -> Union[dict, None]:
        owner_token_data = obj_in.dict()
        owner_token = await self.model.create(**owner_token_data)
        return owner_token


owner_token = CRUDOwnerToken(OwnerToken)
