from fastapi import APIRouter

from app.api.endpoints import employee, owner, reparation_detail, root, vehicle

api_router = APIRouter()
api_router.include_router(root.router)
api_router.include_router(employee.router, prefix="/employees", tags=["employees"])
api_router.include_router(owner.router, prefix="/owners", tags=["owners"])
api_router.include_router(vehicle.router, prefix="/vehicles", tags=["vehicles"])
api_router.include_router(reparation_detail.router, prefix="/details", tags=["details"])
