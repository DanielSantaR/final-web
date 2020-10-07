from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.user import (
    AuthUser,
    CompleteUser,
    CreateUserBase,
    PayloadUser,
    UpdateUser,
    UpdateUserBase,
    UserCreated,
    UserResponse,
)
from app.schemas.user_x_department import (
    PayloadUserXDepartment,
    UpdateUserXDepartment,
    UserXDepartmentResponse,
)
from app.services.user import user_service
from app.services.user_x_department import user_x_department_service

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
    if user:
        user_data = user_in.dict()
        user_data["user_"] = user.id
        user_complete = CompleteUser(**user_data)
        await user_x_department_service.create_user_x_department(
            user_x_department=user_complete
        )
    return user


@router.post(
    "/auth/",
    response_class=JSONResponse,
    response_model=UserResponse,
    status_code=200,
    responses={
        200: {"description": "users found"},
        401: {"description": "User unauthorized"},
    },
)
async def auth_user(*, user_in: AuthUser):
    users = await user_service.auth_user(user=user_in)
    if users:
        return users
    return []


@router.post(
    "/get-all/{department_id}/",
    response_class=JSONResponse,
    response_model=List[UserResponse],
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *, user_in: PayloadUser, department_id: int, skip: int = 0, limit: int = 99999
):
    users = await user_service.get_all(
        user=user_in, department_id=department_id, skip=skip, limit=limit
    )
    if users:
        return users
    return []


@router.get(
    "/user-id/{user_id}/",
    response_class=JSONResponse,
    response_model=UserResponse,
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
    },
)
async def get_byid(*, user_id: int):
    user = await user_service.get_user_by_id(user_id=user_id)
    if not user:
        return JSONResponse(status_code=404, content={"detail": "No user found"})
    return user


@router.delete(
    "/{user_id}/",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "User deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
    },
)
async def remove(*, user_id: int):
    user_remove = await user_service.remove_user(user_id=user_id)
    status_code = 204 if user_remove == 1 else 404
    return JSONResponse(status_code=status_code, content=user_remove)


@router.delete(
    "/{department_id}/{user_id}/{rol_id}/",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "User deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
    },
)
async def remove_rol_x_user(*, department_id: int, rol_id: int, user_id: int):
    user_remove = await user_x_department_service.remove_rol_x_user(
        department_id=department_id, rol_id=rol_id, user_id=user_id,
    )
    status_code = 204 if user_remove == 1 else 404
    return JSONResponse(status_code=status_code, content=user_remove)


@router.put(
    "/{department_id}/{user_id}/{rol_id}/",
    response_class=JSONResponse,
    response_model=UserCreated,
    status_code=200,
    responses={
        200: {"description": "User updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
    },
)
async def update(
    *, department_id: int, user_id: int, rol_id: int, user_in: UpdateUserBase
):
    user_data = user_in.dict()
    user_base = UpdateUser(**user_data)
    user = await user_service.update_user(user_id=user_id, new_user=user_base)
    if not user:
        return JSONResponse(status_code=404, content={"detail": "No user found"})
    user_complete = UpdateUserXDepartment(**user_data)
    print(user_complete)
    await user_x_department_service.update_user_x_department(
        department_id=department_id,
        rol_id=rol_id,
        user_id=user_id,
        new_user_x_department=user_complete,
    )
    return user


@router.post(
    "/get-all-user-x-department-x-rol/",
    response_class=JSONResponse,
    response_model=List[UserXDepartmentResponse],
    status_code=200,
    responses={
        200: {"description": "Users found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all_user_x_department_x_rol(
    *,
    user_x_department_x_rol_in: PayloadUserXDepartment,
    skip: int = 0,
    limit: int = 99999
):
    users = await user_x_department_service.get_all(
        user_x_department=user_x_department_x_rol_in, skip=skip, limit=limit
    )
    if users:
        return users
    return []
