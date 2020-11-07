from typing import Any, Dict, List, Optional, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.employee import employee
from app.schemas.employee import CreateEmployee, UpdateEmployee
from app.schemas.search import EmployeeQueryParams

QueryType = TypeVar("QueryType", bound=ICrudBase)


class EmployeeService:
    def __init__(self, employee_queries: QueryType):
        self.__employee_queries = employee_queries

    async def create_employee(self, employee: CreateEmployee) -> Union[dict, None]:
        new_employee_id = await self.__employee_queries.create(obj_in=employee)
        return new_employee_id

    async def auth(self, username: str) -> Union[dict, None]:
        employee = await self.__employee_queries.auth(username=username)
        if employee:
            return employee
        return None

    async def get_employee_by_id(self, employee_id: str) -> Union[dict, None]:
        employee = await self.__employee_queries.get_by_id(identity_card=employee_id)
        if employee:
            return employee
        return None

    async def get_employee_by_username(self, username: str) -> Union[dict, None]:
        employee = await self.__employee_queries.get_by_username(username=username)
        if employee:
            return employee
        return None

    async def get_all(
        self, *, query_args: EmployeeQueryParams, skip: int, limit: int
    ) -> List:
        employee_data = query_args.__dict__
        payload = {
            key: value
            for (key, value) in employee_data.items()
            if value not in [None, ""]
        }
        employees = await self.__employee_queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return employees

    async def update_employee(
        self, employee_id: str, new_employee: UpdateEmployee
    ) -> Optional[Dict[str, Any]]:
        new_employee_data = new_employee.dict()
        payload = {
            key: value
            for (key, value) in new_employee_data.items()
            if value not in [None, ""]
        }
        current_update = await self.__employee_queries.update(
            identity_card=employee_id, obj_in=payload
        )
        return current_update

    async def remove_employee(self, employee_id: str) -> int:
        employee_removed_id = await self.__employee_queries.delete(
            identity_card=employee_id
        )
        return employee_removed_id


employee_service = EmployeeService(employee_queries=employee)
