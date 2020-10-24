from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.schemas.reparation_detail import (
    CreateReparationDetail,
    PayloadReparationDetail,
    ReparationDetailInDB,
    UpdateReparationDetail,
)
from app.services.reparation_detail import reparation_detail_service

router = APIRouter()


@router.post(
    "/",
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


@router.post(
    "/get-all/",
    response_class=JSONResponse,
    response_model=List[ReparationDetailInDB],
    status_code=200,
    responses={
        200: {"description": "Entities found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *, reparation_detail_in: PayloadReparationDetail, skip: int = 0, limit: int = 99999
):
    reparation_details = await reparation_detail_service.get_all(
        reparation_detail=reparation_detail_in, skip=skip, limit=limit
    )
    if reparation_details:
        return reparation_details
    return []


@router.get(
    "/reparation_detail-id/{reparation_detail_id}/",
    response_class=JSONResponse,
    response_model=ReparationDetailInDB,
    status_code=200,
    responses={
        200: {"description": "ReparationDetail found"},
        401: {"description": "User unauthorized"},
        404: {"description": "ReparationDetail not found"},
    },
)
async def get_byid(*, reparation_detail_id: int):
    reparation_detail = await reparation_detail_service.get_reparation_detail_by_id(
        reparation_detail_id=reparation_detail_id
    )
    if not reparation_detail:
        return JSONResponse(
            status_code=404, content={"detail": "No reparation_detail found"}
        )
    return reparation_detail


@router.delete(
    "/{reparation_detail_id}/",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "ReparationDetail deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "ReparationDetail not found"},
    },
)
async def remove(*, reparation_detail_id: int):
    reparation_detail_remove = await reparation_detail_service.remove_reparation_detail(
        reparation_detail_id=reparation_detail_id
    )
    status_code = 204 if reparation_detail_remove == 1 else 404
    return Response(status_code=status_code, content=reparation_detail_remove)


@router.put(
    "/{reparation_detail_id}/",
    response_class=JSONResponse,
    response_model=ReparationDetailInDB,
    status_code=200,
    responses={
        200: {"description": "ReparationDetail updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "ReparationDetail not found"},
    },
)
async def update(
    *, reparation_detail_id: int, reparation_detail_in: UpdateReparationDetail
):
    reparation_detail = await reparation_detail_service.update_reparation_detail(
        reparation_detail_id=reparation_detail_id,
        new_reparation_detail=reparation_detail_in,
    )
    if not reparation_detail:
        return JSONResponse(
            status_code=404, content={"detail": "No reparation_detail found"}
        )
    return reparation_detail
