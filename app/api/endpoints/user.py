from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.user import CreateUserBase, UserCreated
from app.services.user import user_service

router = APIRouter()


@router.post(
    "/",
    response_class=JSONResponse,
    response_model=UserCreated,
    status_code=201,
    responses={201: {"description": " User created"}},
)
async def create(*, user_in: CreateUserBase):
    user = await user_service.create_user(user=user_in)
    return user
