from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.schemas.owner_token import CreateOwnerToken, OwnerTokenInDB
from app.schemas.search import OwnerTokenQueryParams
from app.services.owner_token import owner_token_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=OwnerTokenInDB,
    status_code=201,
    responses={201: {"description": " Owner Token created"}},
)
async def create(*, owner_token_in: CreateOwnerToken):
    owner_token = await owner_token_service.create_owner_token(
        owner_token=owner_token_in
    )
    return owner_token


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[OwnerTokenInDB],
    status_code=200,
    responses={
        200: {"description": "Owner Tokens found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *, query_args: OwnerTokenQueryParams = Depends(), skip: int = 0, limit: int = 99999
):
    employees = await owner_token_service.get_all(
        query_args=query_args, skip=skip, limit=limit
    )
    if employees:
        return employees
    return []


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=OwnerTokenInDB,
    status_code=200,
    responses={
        200: {"description": "Owner Token found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner Token not found"},
    },
)
async def get_byid(*, id: str):
    owner_token = await owner_token_service.get_owner_token_by_id(owner_token_id=id)
    if not owner_token:
        return JSONResponse(status_code=404, content={"detail": "No owner token found"})
    return owner_token


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Owner Token deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Owner Token not found"},
    },
)
async def remove(*, id: str):
    owner_token_remove = await owner_token_service.remove_owner_token(owner_token_id=id)
    status_code = 204 if owner_token_remove == 1 else 404
    return Response(status_code=status_code)
