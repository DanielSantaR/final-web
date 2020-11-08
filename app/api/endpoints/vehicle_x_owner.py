from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.schemas.search import VehicleXOwnerQueryParams
from app.schemas.vehicle_x_owner import (
    CreateVehicleXOwner,
    UpdateVehicleXOwner,
    VehicleXOwnerInDB,
)
from app.services.vehicle_x_owner import vehicle_x_owner_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=VehicleXOwnerInDB,
    status_code=201,
    responses={201: {"description": " VehicleXOwner created"}},
)
async def create(*, vehicle_x_owner_in: CreateVehicleXOwner):
    vehicle_x_owner = await vehicle_x_owner_service.create_vehicle_x_owner(
        vehicle_x_owner=vehicle_x_owner_in
    )
    return vehicle_x_owner


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=VehicleXOwnerInDB,
    status_code=200,
    responses={
        200: {"description": "VehicleXOwner found"},
        401: {"description": "User unauthorized"},
        404: {"description": "VehicleXOwner not found"},
    },
)
async def get_byid(*, id: int):
    vehicle_x_owner = await vehicle_x_owner_service.get_vehicle_x_owner_by_id(
        vehicle_x_owner_id=id
    )
    if not vehicle_x_owner:
        return JSONResponse(
            status_code=404, content={"detail": "No vehicle_x_owner found"}
        )
    return vehicle_x_owner


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[VehicleXOwnerInDB],
    status_code=200,
    responses={
        200: {"description": "VehicleXOwners found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *,
    query_args: VehicleXOwnerQueryParams = Depends(),
    skip: int = 0,
    limit: int = 99999
):
    employees = await vehicle_x_owner_service.get_all(
        query_args=query_args, skip=skip, limit=limit
    )
    if employees:
        return employees
    return []


@router.put(
    "/{id}",
    response_class=JSONResponse,
    response_model=VehicleXOwnerInDB,
    status_code=200,
    responses={
        200: {"description": "VehicleXOwner updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "VehicleXOwner not found"},
    },
)
async def update(*, id: str, vehicle_x_owner_in: UpdateVehicleXOwner):
    vehicle_x_owner = await vehicle_x_owner_service.update_vehicle_x_owner(
        vehicle_x_owner_id=id, new_vehicle_x_owner=vehicle_x_owner_in
    )
    if not vehicle_x_owner:
        return JSONResponse(
            status_code=404, content={"detail": "No vehicle_x_owner found"}
        )
    return vehicle_x_owner


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "VehicleXOwner deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "VehicleXOwner not found"},
    },
)
async def remove(*, id: str):
    vehicle_x_owner_remove = await vehicle_x_owner_service.remove_vehicle_x_owner(
        vehicle_x_owner_id=id
    )
    status_code = 204 if vehicle_x_owner_remove == 1 else 404
    return Response(status_code=status_code)
