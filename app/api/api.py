from fastapi import APIRouter

from app.api.endpoints import employee, owner, reparation_detail, vehicle

# from app.api.endpoints import br

api_router = APIRouter()
api_router.include_router(employee.router, prefix="/employee", tags=["employee"])
api_router.include_router(owner.router, prefix="/owner", tags=["owner"])
api_router.include_router(
    reparation_detail.router, prefix="/reparation_detail", tags=["reparation_detail"]
)
api_router.include_router(vehicle.router, prefix="/vehicle", tags=["vehicle"])
# api_router.include_router(br.router, prefix="/br", tags=["br"])
