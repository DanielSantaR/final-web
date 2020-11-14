from typing import Any, Dict, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.reparation_detail import ReparationDetail
from app.schemas.reparation_detail import CreateReparationDetail, UpdateReparationDetail


class CRUDReparationDetail(
    CRUDBase[ReparationDetail, CreateReparationDetail, UpdateReparationDetail]
):
    async def get_by_id(self, *, id: int) -> Union[dict, None]:
        model = await self.model.filter(id=id).first().values()
        if model:
            return model[0]
        return None

    async def update(self, *, id: int, obj_in: Dict[str, Any]) -> Union[dict, None]:
        if not obj_in:
            model = await self.model.filter(id=id).first().values()
        else:
            model = await self.model.filter(id=id).update(**obj_in)
        if model:
            update_model = await self.model.filter(id=id).first().values()
            model_m = self.model(**update_model[0])
            update_fields = list(update_model[0].keys())
            await model_m.save(update_fields=update_fields)
            return update_model[0]
        return None

    async def delete(self, *, id: int) -> int:
        model = await self.model.filter(id=id).first().delete()
        return model

    async def create(self, *, obj_in: CreateReparationDetail) -> Union[dict, None]:
        reparation_detail_data = obj_in.dict()
        detail = await self.model.create(
            **reparation_detail_data,
        )

        return detail


reparation_detail = CRUDReparationDetail(ReparationDetail)
