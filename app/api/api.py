from fastapi import APIRouter

from app.api.endpoints import (
    employee,
    owner,
    owner_token,
    reparation_detail,
    root,
    vehicle,
    vehicle_x_owner,
)

api_router = APIRouter()
api_router.include_router(root.router)
api_router.include_router(employee.router, prefix="/employees", tags=["employees"])
api_router.include_router(owner.router, prefix="/owners", tags=["owners"])
api_router.include_router(vehicle.router, prefix="/vehicles", tags=["vehicles"])
api_router.include_router(
    vehicle_x_owner.router, prefix="/vehicles-x-owners", tags=["vehicles-x-owners"]
)
api_router.include_router(reparation_detail.router, prefix="/details", tags=["details"])
api_router.include_router(
    owner_token.router, prefix="/owner-tokens", tags=["owner-tokens"]
)
