from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.reparation_detail import ReparationDetail
from app.schemas.reparation_detail import CreateReparationDetail, UpdateReparationDetail


class CRUDReparationDetail(
    CRUDBase[ReparationDetail, CreateReparationDetail, UpdateReparationDetail]
):
    ...


reparation_detail = CRUDReparationDetail(ReparationDetail)
