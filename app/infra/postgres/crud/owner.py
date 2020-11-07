from typing import Any, Dict, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.owner import Owner
from app.schemas.owner import CreateOwner, UpdateOwner
from app.utils.get_keys import get_right_keys

DB_KEYS = {
    "creation_employee": "creation_employee_id",
    "update_employee": "update_employee_id",
    "vehicle": "vehicle_id",
}


class CRUDOwner(CRUDBase[Owner, CreateOwner, UpdateOwner]):
    async def get_by_id(self, *, identity_card: str) -> Union[dict, None]:
        model = await self.model.filter(identity_card=identity_card).first().values()
        if model:
            return model[0]
        return None

    async def update(
        self, *, identity_card: str, obj_in: Dict[str, Any]
    ) -> Union[dict, None]:
        obj_in = get_right_keys(payload=obj_in, db_keys=DB_KEYS)
        if not obj_in:
            model = (
                await self.model.filter(identity_card=identity_card).first().values()
            )
        else:
            model = await self.model.filter(identity_card=identity_card).update(
                **obj_in
            )
        if model:
            update_model = (
                await self.model.filter(identity_card=identity_card).first().values()
            )
            model_m = self.model(**update_model[0])
            update_fields = list(update_model[0].keys())
            await model_m.save(update_fields=update_fields)
            return update_model[0]
        return None

    async def delete(self, *, identity_card: str) -> int:
        model = await self.model.filter(identity_card=identity_card).first().delete()
        return model

    async def create(self, *, obj_in: CreateOwner) -> Union[dict, None]:
        owner_data = obj_in.dict()
        owner_data = get_right_keys(payload=owner_data, db_keys=DB_KEYS)
        owner = await self.model.create(**owner_data,)
        return owner


owner = CRUDOwner(Owner)
