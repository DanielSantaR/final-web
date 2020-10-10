from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.owner import Owner
from app.schemas.owner import CreateOwner, UpdateOwner


class CRUDOwner(CRUDBase[Owner, CreateOwner, UpdateOwner]):
    ...


owner = CRUDOwner(Owner)
