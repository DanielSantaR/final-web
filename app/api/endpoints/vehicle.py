from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.schemas.vehicle import (
    CreateVehicle,
    PayloadVehicle,
    UpdateVehicle,
    VehicleInDB,
)
from app.schemas.vehicle_x_owner import CreateVehicleXOwner
from app.services.vehicle import vehicle_service
from app.services.vehicle_x_owner import vehicle_x_owner

router = APIRouter()


@router.post(
    "/",
    response_class=JSONResponse,
    response_model=VehicleInDB,
    status_code=201,
    responses={201: {"description": " Vehicle created"}},
)
async def create(*, vehicle_in: CreateVehicle):
    vehicle = await vehicle_service.create_vehicle(vehicle=vehicle_in)
    if vehicle:
        for owner in vehicle_in.owners:
            owner_vehicle = CreateVehicleXOwner(vehicle=vehicle_in.plate, owner=owner)
            await vehicle_x_owner.create(obj_in=owner_vehicle)
    return vehicle


@router.post(
    "/get-all/",
    response_class=JSONResponse,
    response_model=List[VehicleInDB],
    status_code=200,
    responses={
        200: {"description": "Entities found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(*, vehicle_in: PayloadVehicle, skip: int = 0, limit: int = 99999):
    vehicles = await vehicle_service.get_all(vehicle=vehicle_in, skip=skip, limit=limit)
    if vehicles:
        return vehicles
    return []


@router.get(
    "/vehicle-id/{vehicle_id}/",
    response_class=JSONResponse,
    response_model=VehicleInDB,
    status_code=200,
    responses={
        200: {"description": "Vehicle found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Vehicle not found"},
    },
)
async def get_byid(*, vehicle_id: str):
    vehicle = await vehicle_service.get_vehicle_by_id(vehicle_id=vehicle_id)
    if not vehicle:
        return JSONResponse(status_code=404, content={"detail": "No vehicle found"})
    return vehicle


@router.delete(
    "/{vehicle_id}/",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Vehicle deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Vehicle not found"},
    },
)
async def remove(*, vehicle_id: str):
    vehicle_remove = await vehicle_service.remove_vehicle(vehicle_id=vehicle_id)
    status_code = 204 if vehicle_remove == 1 else 404
    return Response(status_code=status_code)


@router.put(
    "/{vehicle_id}/",
    response_class=JSONResponse,
    response_model=VehicleInDB,
    status_code=200,
    responses={
        200: {"description": "Vehicle updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Vehicle not found"},
    },
)
async def update(*, vehicle_id: str, vehicle_in: UpdateVehicle):
    vehicle = await vehicle_service.update_vehicle(
        vehicle_id=vehicle_id, new_vehicle=vehicle_in
    )
    if not vehicle:
        return JSONResponse(status_code=404, content={"detail": "No vehicle found"})
    return vehicle
