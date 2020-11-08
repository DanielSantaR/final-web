from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.schemas.reparation_detail import (
    CreateReparationDetail,
    ReparationDetailInDB,
    UpdateReparationDetail,
)
from app.schemas.search import ReparationDetailQueryParams
from app.services.reparation_detail import reparation_detail_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=ReparationDetailInDB,
    status_code=201,
    responses={201: {"description": " ReparationDetail created"}},
)
async def create(*, reparation_detail_in: CreateReparationDetail):
    reparation_detail = await reparation_detail_service.create_reparation_detail(
        reparation_detail=reparation_detail_in
    )
    return reparation_detail


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=ReparationDetailInDB,
    status_code=200,
    responses={
        200: {"description": "ReparationDetail found"},
        401: {"description": "User unauthorized"},
        404: {"description": "ReparationDetail not found"},
    },
)
async def get_byid(*, id: int):
    reparation_detail = await reparation_detail_service.get_reparation_detail_by_id(
        reparation_detail_id=id
    )
    if not reparation_detail:
        return JSONResponse(
            status_code=404, content={"detail": "No reparation_detail found"}
        )
    return reparation_detail


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[ReparationDetailInDB],
    status_code=200,
    responses={
        200: {"description": "Details found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *,
    query_args: ReparationDetailQueryParams = Depends(),
    skip: int = 0,
    limit: int = 99999
):
    employees = await reparation_detail_service.get_all(
        query_args=query_args, skip=skip, limit=limit
    )
    if employees:
        return employees
    return []


@router.put(
    "/{id}",
    response_class=JSONResponse,
    response_model=ReparationDetailInDB,
    status_code=200,
    responses={
        200: {"description": "ReparationDetail updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "ReparationDetail not found"},
    },
)
async def update(*, id: int, reparation_detail_in: UpdateReparationDetail):
    reparation_detail = await reparation_detail_service.update_reparation_detail(
        reparation_detail_id=id, new_reparation_detail=reparation_detail_in,
    )
    if not reparation_detail:
        return JSONResponse(
            status_code=404, content={"detail": "No reparation_detail found"}
        )
    return reparation_detail


@router.delete(
    "/{id}",
    response_class=JSONResponse,
    status_code=204,
    responses={
        204: {"description": "ReparationDetail deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "ReparationDetail not found"},
    },
)
async def remove(*, id: int):
    reparation_detail_remove = await reparation_detail_service.remove_reparation_detail(
        reparation_detail_id=id
    )
    status_code = 204 if reparation_detail_remove == 1 else 404
    return status_code
