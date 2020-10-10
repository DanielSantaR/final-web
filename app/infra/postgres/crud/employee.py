from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.employee import Employee
from app.schemas.employee import CreateEmployee, UpdateEmployee


class CRUDEmployee(CRUDBase[Employee, CreateEmployee, UpdateEmployee]):
    ...


employee = CRUDEmployee(Employee)
