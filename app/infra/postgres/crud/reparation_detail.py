from typing import Any, Dict, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.reparation_detail import ReparationDetail
from app.schemas.reparation_detail import CreateReparationDetail, UpdateReparationDetail
from app.utils.get_keys import get_right_keys

DB_KEYS = {"vehicle": "vehicle_id", "employee": "employee_id"}


class CRUDReparationDetail(
    CRUDBase[ReparationDetail, CreateReparationDetail, UpdateReparationDetail]
):
    async def get_by_id(self, *, vehicles: str, employees: str) -> Union[dict, None]:
        model = (
            await self.model.filter(vehicles=vehicles, employees=employees)
            .first()
            .values()
        )
        if model:
            return model[0]
        return None

    async def update(
        self, *, vehicles: str, employees: str, obj_in: Dict[str, Any]
    ) -> Union[dict, None]:
        model = await self.model.filter(vehicles=vehicles, employees=employees).update(
            **obj_in
        )
        if model:
            update_model = (
                await self.model.filter(vehicles=vehicles, employees=employees)
                .first()
                .values()
            )
            model_m = self.model(**update_model[0])
            update_fields = list(update_model[0].keys())
            await model_m.save(update_fields=update_fields)
            return update_model[0]
        return None

    async def delete(self, *, vehicles: str, employees: str) -> int:
        model = (
            await self.model.filter(vehicles=vehicles, employees=employees)
            .first()
            .delete()
        )
        return model

    async def create(self, *, obj_in: CreateReparationDetail) -> Union[dict, None]:
        reparation_detail_data = obj_in.dict()
        reparation_detail_data = get_right_keys(
            payload=reparation_detail_data, db_keys=DB_KEYS
        )
        detail = await self.model.create(**reparation_detail_data,)

        return detail


reparation_detail = CRUDReparationDetail(ReparationDetail)
