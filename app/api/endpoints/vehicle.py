from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.schemas.search import VehicleQueryParams
from app.schemas.vehicle import CreateVehicle, UpdateVehicle, VehicleInDB
from app.services.vehicle import vehicle_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=VehicleInDB,
    status_code=201,
    responses={201: {"description": " Vehicle created"}},
)
async def create(*, vehicle_in: CreateVehicle):
    vehicle = await vehicle_service.create_vehicle(vehicle=vehicle_in)
    return vehicle


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[VehicleInDB],
    status_code=200,
    responses={
        200: {"description": "Vehicles found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *, query_args: VehicleQueryParams = Depends(), skip: int = 0, limit: int = 99999
):
    employees = await vehicle_service.get_all(
        query_args=query_args, skip=skip, limit=limit
    )
    if employees:
        return employees
    return []


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=VehicleInDB,
    status_code=200,
    responses={
        200: {"description": "Vehicle found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Vehicle not found"},
    },
)
async def get_byid(*, id: str):
    vehicle = await vehicle_service.get_vehicle_by_id(vehicle_id=id)
    if not vehicle:
        return JSONResponse(status_code=404, content={"detail": "No vehicle found"})
    return vehicle


@router.patch(
    "/{id}",
    response_class=JSONResponse,
    response_model=VehicleInDB,
    status_code=200,
    responses={
        200: {"description": "Vehicle updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Vehicle not found"},
    },
)
async def update(*, id: str, vehicle_in: UpdateVehicle):
    vehicle = await vehicle_service.update_vehicle(
        vehicle_id=id, new_vehicle=vehicle_in
    )
    if not vehicle:
        return JSONResponse(status_code=404, content={"detail": "No vehicle found"})
    return vehicle


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Vehicle deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Vehicle not found"},
    },
)
async def remove(*, id: str):
    vehicle_remove = await vehicle_service.remove_vehicle(vehicle_id=id)
    status_code = 204 if vehicle_remove == 1 else 404
    return Response(status_code=status_code)
