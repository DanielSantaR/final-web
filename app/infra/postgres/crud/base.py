from typing import Any, Dict, List, TypeVar, Union

from pydantic import BaseModel
from tortoise import models

from app.crud.base import ICrudBase

ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(ICrudBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    async def get_by_id(self, *, id: int) -> Union[dict, None]:
        model = await self.model.filter(id=id).first().values()
        if model:
            return model[0]
        return None

    async def get_all(
        self,
        *,
        payload: dict = None,
        skip: int = 0,
        limit: int = 10,
    ) -> List:
        if payload:
            model = (
                await self.model.filter(**payload)
                .offset(skip)
                .limit(limit)
                .all()
                .values()
            )
        else:
            model = await self.model.all().offset(skip).limit(limit).values()
        return model

    async def create(self, *, obj_in: CreateSchemaType) -> Union[dict, None]:
        obj_in_data = obj_in.dict()
        model = self.model(**obj_in_data)
        await model.save()
        return model

    async def update(self, *, id: int, obj_in: Dict[str, Any]) -> Union[dict, None]:
        if not obj_in:
            model = await self.model.filter(id=id).first().values()
        else:
            model = await self.model.filter(id=id).update(**obj_in)
        if model:
            update_model = await self.model.filter(id=id).first().values()
            model_m = self.model(**update_model[0])
            update_fields = list(update_model[0].keys())
            await model_m.save(update_fields=update_fields)
            return update_model[0]
        return None

    async def delete(self, *, id: int) -> int:
        model = await self.model.filter(id=id).first().delete()
        return model
