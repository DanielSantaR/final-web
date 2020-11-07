from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.schemas.owner import CreateOwner, OwnerInDB, UpdateOwner
from app.schemas.search import OwnerQueryParams
from app.services.owner import owner_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=OwnerInDB,
    status_code=201,
    responses={201: {"description": " Owner created"}},
)
async def create(*, owner_in: CreateOwner):
    owner = await owner_service.create_owner(owner=owner_in)
    return owner


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[OwnerInDB],
    status_code=200,
    responses={
        200: {"description": "Owners found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *, query_args: OwnerQueryParams = Depends(), skip: int = 0, limit: int = 99999
):
    employees = await owner_service.get_all(
        query_args=query_args, skip=skip, limit=limit
    )
    if employees:
        return employees
    return []


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=OwnerInDB,
    status_code=200,
    responses={
        200: {"description": "Owner found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner not found"},
    },
)
async def get_byid(*, id: str):
    owner = await owner_service.get_owner_by_id(owner_id=id)
    if not owner:
        return JSONResponse(status_code=404, content={"detail": "No owner found"})
    return owner


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Owner deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner not found"},
    },
)
async def remove(*, id: str):
    owner_remove = await owner_service.remove_owner(owner_id=id)
    status_code = 204 if owner_remove == 1 else 404
    return Response(status_code=status_code)


@router.put(
    "/{id}",
    response_class=JSONResponse,
    response_model=OwnerInDB,
    status_code=200,
    responses={
        200: {"description": "Owner updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner not found"},
    },
)
async def update(*, id: str, owner_in: UpdateOwner):
    owner = await owner_service.update_owner(owner_id=id, new_owner=owner_in)
    if not owner:
        return JSONResponse(status_code=404, content={"detail": "No owner found"})
    return owner
