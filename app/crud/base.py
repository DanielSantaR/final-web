from abc import abstractmethod
from typing import Any, Dict, Generic, TypeVar

from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class ICrudBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    @abstractmethod
    def __init__(self, model: Any):
        raise NotImplementedError

    @abstractmethod
    async def create(self, obj_in: CreateSchemaType) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, obj_in: Dict[str, Any]) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *, payload: dict, skip: int, limit: int) -> Any:
        raise NotImplementedError
