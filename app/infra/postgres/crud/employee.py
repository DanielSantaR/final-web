from typing import Any, Dict, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.employee import Employee
from app.schemas.employee import CreateEmployee, UpdateEmployee


class CRUDEmployee(CRUDBase[Employee, CreateEmployee, UpdateEmployee]):
    async def auth(self, *, username: str) -> Union[dict, None]:
        model = await self.model.filter(username=username).first().values()
        if model:
            return model[0]
        return None

    async def get_by_id(self, *, identity_card: str) -> Union[dict, None]:
        model = await self.model.filter(identity_card=identity_card).first().values()
        if model:
            return model[0]
        return None

    async def get_by_username(self, *, username: str) -> Union[dict, None]:
        model = await self.model.filter(username=username).first().values()
        if model:
            return model[0]
        return None

    async def update(
        self, *, identity_card: str, obj_in: Dict[str, Any]
    ) -> Union[dict, None]:
        if "role" in obj_in:
            obj_in["role"] = obj_in["role"].value
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


employee = CRUDEmployee(Employee)
