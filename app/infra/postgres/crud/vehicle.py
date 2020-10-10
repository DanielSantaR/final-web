from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.vehicle import Vehicle
from app.schemas.vehicle import CreateVehicle, UpdateVehicle


class CRUDVehicle(CRUDBase[Vehicle, CreateVehicle, UpdateVehicle]):
    ...


vehicle = CRUDVehicle(Vehicle)
