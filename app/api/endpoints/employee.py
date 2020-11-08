from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.schemas.employee import (
    AuthEmployee,
    CreateEmployee,
    EmployeeInDB,
    UpdateEmployee,
)
from app.schemas.search import EmployeeQueryParams
from app.services.employee import employee_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=EmployeeInDB,
    status_code=201,
    responses={201: {"description": " Employee created"}},
)
async def create(*, employee_in: CreateEmployee):
    employee = await employee_service.create_employee(employee=employee_in)
    return employee


@router.get(
    "/auth/{username}",
    response_class=JSONResponse,
    response_model=AuthEmployee,
    status_code=200,
    responses={
        200: {"description": "Employee found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def auth(*, username: str):
    employee = await employee_service.auth(username=username)
    if not employee:
        return JSONResponse(status_code=404, content={"detail": "No employee found"})
    return employee


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=EmployeeInDB,
    status_code=200,
    responses={
        200: {"description": "Employee found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def get_byid(*, id: str):
    employee = await employee_service.get_employee_by_id(employee_id=id)
    if not employee:
        return JSONResponse(status_code=404, content={"detail": "No employee found"})
    return employee


@router.get(
    "/username/{username}",
    response_class=JSONResponse,
    response_model=EmployeeInDB,
    status_code=200,
    responses={
        200: {"description": "Employee found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def get_by_username(*, username: str):
    employee = await employee_service.get_employee_by_username(username=username)
    if not employee:
        return JSONResponse(status_code=404, content={"detail": "No employee found"})
    return employee


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[EmployeeInDB],
    status_code=200,
    responses={
        200: {"description": "Employees found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *, query_args: EmployeeQueryParams = Depends(), skip: int = 0, limit: int = 99999
):
    employees = await employee_service.get_all(
        query_args=query_args, skip=skip, limit=limit
    )
    if employees:
        return employees
    return []


@router.put(
    "/{id}",
    response_class=JSONResponse,
    response_model=EmployeeInDB,
    status_code=200,
    responses={
        200: {"description": "Employee updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def update(*, id: str, employee_in: UpdateEmployee):
    employee = await employee_service.update_employee(
        employee_id=id, new_employee=employee_in
    )
    if not employee:
        return JSONResponse(status_code=404, content={"detail": "No employee found"})
    return employee


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Employee deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Employee not found"},
    },
)
async def remove(*, id: str):
    employee_remove = await employee_service.remove_employee(employee_id=id)
    status_code = 204 if employee_remove == 1 else 404
    return Response(status_code=status_code)
