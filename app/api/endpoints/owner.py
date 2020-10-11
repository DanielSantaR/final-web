from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.owner import CreateOwner, OwnerInDB, PayloadOwner, UpdateOwner
from app.services.owner import owner_service

router = APIRouter()


@router.post(
    "/",
    response_class=JSONResponse,
    response_model=OwnerInDB,
    status_code=201,
    responses={201: {"description": " Owner created"}},
)
async def create(*, owner_in: CreateOwner):
    owner = await owner_service.create_owner(owner=owner_in)
    return owner


@router.post(
    "/get-all/",
    response_class=JSONResponse,
    response_model=List[OwnerInDB],
    status_code=200,
    responses={
        200: {"description": "Entities found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(*, owner_in: PayloadOwner, skip: int = 0, limit: int = 99999):
    owners = await owner_service.get_all(owner=owner_in, skip=skip, limit=limit)
    if owners:
        return owners
    return []


@router.get(
    "/owner-id/{owner_id}/",
    response_class=JSONResponse,
    response_model=OwnerInDB,
    status_code=200,
    responses={
        200: {"description": "Owner found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner not found"},
    },
)
async def get_byid(*, owner_id: int):
    owner = await owner_service.get_owner_by_id(owner_id=owner_id)
    if not owner:
        return JSONResponse(status_code=404, content={"detail": "No owner found"})
    return owner


@router.delete(
    "/{owner_id}/",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "Owner deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner not found"},
    },
)
async def remove(*, owner_id: int):
    owner_remove = await owner_service.remove_owner(owner_id=owner_id)
    status_code = 204 if owner_remove == 1 else 404
    return JSONResponse(status_code=status_code, content=owner_remove)


@router.put(
    "/{owner_id}/",
    response_class=JSONResponse,
    response_model=OwnerInDB,
    status_code=200,
    responses={
        200: {"description": "Owner updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner not found"},
    },
)
async def update(*, owner_id: int, owner_in: UpdateOwner):
    owner = await owner_service.update_owner(owner_id=owner_id, new_owner=owner_in)
    if not owner:
        return JSONResponse(status_code=404, content={"detail": "No owner found"})
    return owner
