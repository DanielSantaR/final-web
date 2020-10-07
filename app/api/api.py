from fastapi import APIRouter

from app.api.endpoints import root, user

api_router = APIRouter()

api_router.include_router(root.router)
api_router.include_router(user.router, prefix="/user", tags=["user"])
