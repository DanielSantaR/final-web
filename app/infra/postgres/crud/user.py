from typing import Any, Dict, List, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.user import User
from app.schemas.user import AuthUser, CreateUser, UpdateUser


class CRUDUser(CRUDBase[User, CreateUser, UpdateUser]):
    async def create(self, *, obj_in: CreateUser) -> Union[dict, None]:
        user_data = obj_in.dict()
        user = await self.model.create(**user_data)
        return user

    async def get_by_id(self, *, id: int) -> Union[dict, None]:
        model = await self.model.filter(id=id).all()
        if model:
            return model[0]
        return None

    async def auth_user(self, *, user: AuthUser) -> Union[dict, None]:
        model = await self.model.filter(username=user.username).all()
        if model:
            if model[0].password == user.password:
                return model[0]
            return None
        return None

    async def get_all(
        self,
        *,
        payload: dict = None,
        department_id: int,
        skip: int = 0,
        limit: int = 10,
    ) -> List:
        if payload:
            model = (
                await self.model.filter(
                    user_x_departments__department_id=department_id, **payload
                )
                .offset(skip)
                .limit(limit)
                .all()
            )
        else:
            model = (
                await self.model.filter(user_x_departments__department_id=department_id)
                .all()
                .offset(skip)
                .limit(limit)
            )
        return model

    async def update(
        self, *, id: int, obj_in: Dict[UpdateUser, Any]
    ) -> Union[dict, None]:
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

    async def delete_user(self, *, user_id: int) -> int:
        model = await self.model.filter(id=user_id).first().delete()
        return model


user = CRUDUser(User)
