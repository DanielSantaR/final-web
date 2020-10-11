from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.employee import (
    CreateEmployee,
    EmployeeInDB,
    PayloadEmployee,
    UpdateEmployee,
)
from app.services.employee import employee_service

router = APIRouter()


@router.post(
    "/",
    response_class=JSONResponse,
    response_model=EmployeeInDB,
    status_code=201,
    responses={201: {"description": " Employee created"}},
)
async def create(*, employee_in: CreateEmployee):
    employee = await employee_service.create_employee(employee=employee_in)
    return employee


@router.post(
    "/get-all/",
    response_class=JSONResponse,
    response_model=List[EmployeeInDB],
    status_code=200,
    responses={
        200: {"description": "Entities found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(*, employee_in: PayloadEmployee, skip: int = 0, limit: int = 99999):
    employees = await employee_service.get_all(
        employee=employee_in, skip=skip, limit=limit
    )
    if employees:
        return employees
    return []


@router.get(
    "/employee-id/{employee_id}/",
    response_class=JSONResponse,
    response_model=EmployeeInDB,
    status_code=200,
    responses={
        200: {"description": "Employee found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def get_byid(*, employee_id: str):
    employee = await employee_service.get_employee_by_id(employee_id=employee_id)
    if not employee:
        return JSONResponse(status_code=404, content={"detail": "No employee found"})
    return employee


@router.delete(
    "/{employee_id}/",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "Employee deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def remove(*, employee_id: str):
    employee_remove = await employee_service.remove_employee(employee_id=employee_id)
    status_code = 204 if employee_remove == 1 else 404
    return JSONResponse(status_code=status_code, content=employee_remove)


@router.put(
    "/{employee_id}/",
    response_class=JSONResponse,
    response_model=EmployeeInDB,
    status_code=200,
    responses={
        200: {"description": "Employee updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def update(*, employee_id: str, employee_in: UpdateEmployee):
    employee = await employee_service.update_employee(
        employee_id=employee_id, new_employee=employee_in
    )
    if not employee:
        return JSONResponse(status_code=404, content={"detail": "No employee found"})
    return employee
