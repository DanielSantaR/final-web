from typing import Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.owner import Owner
from app.schemas.owner import CreateOwner, UpdateOwner


class CRUDOwner(CRUDBase[Owner, CreateOwner, UpdateOwner]):
    async def create(self, *, obj_in: CreateOwner) -> Union[dict, None]:
        owner_data = obj_in.dict()
        owner_data["creation_employee_id"] = owner_data.pop("creation_employee", None)
        owner_data["update_employee_id"] = owner_data.pop("update_employee", None)
        owner = await self.model.create(**owner_data,)
        return owner


owner = CRUDOwner(Owner)
