""" from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.br import BRInDB, CreateBR, PayloadBR, UpdateBR
from app.services.br import br_service

router = APIRouter()


@router.post(
    "/",
    response_class=JSONResponse,
    response_model=BRInDB,
    status_code=201,
    responses={201: {"description": " BR created"}},
)
async def create(*, br_in: CreateBR):
    br = await br_service.create_br(br=br_in)
    return br


@router.post(
    "/get-all/",
    response_class=JSONResponse,
    response_model=List[BRInDB],
    status_code=200,
    responses={
        200: {"description": "Entities found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(*, br_in: PayloadBR, skip: int = 0, limit: int = 99999):
    brs = await br_service.get_all(br=br_in, skip=skip, limit=limit)
    if brs:
        return brs
    return []


@router.get(
    "/br-id/{br_id}/",
    response_class=JSONResponse,
    response_model=BRInDB,
    status_code=200,
    responses={
        200: {"description": "BR found"},
        401: {"description": "User unauthorized"},
        404: {"description": "BR not found"},
    },
)
async def get_byid(*, br_id: int):
    br = await br_service.get_br_by_id(br_id=br_id)
    if not br:
        return JSONResponse(status_code=404, content={"detail": "No br found"})
    return br


@router.delete(
    "/{br_id}/",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "BR deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "BR not found"},
    },
)
async def remove(*, br_id: int):
    br_remove = await br_service.remove_br(br_id=br_id)
    status_code = 204 if br_remove == 1 else 404
    return JSONResponse(status_code=status_code, content=br_remove)


@router.put(
    "/{br_id}/",
    response_class=JSONResponse,
    response_model=BRInDB,
    status_code=200,
    responses={
        200: {"description": "BR updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "BR not found"},
    },
)
async def update(*, br_id: int, br_in: UpdateBR):
    br = await br_service.update_br(br_id=br_id, new_br=br_in)
    if not br:
        return JSONResponse(status_code=404, content={"detail": "No br found"})
    return br
 """
